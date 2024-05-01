# Завдання 2
# Користувач вводить з клавіатури шлях до файлу. Після
# чого запускаються три потоки. Перший потік заповнює файл
# випадковими числами. Два інші потоки очікують на заповнення. Коли файл заповнений, обидва потоки стартують.
# Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі. Результати пошуку
# кожен потік має записати у новий файл. Виведіть на екран
# статистику виконаних операцій.
import json
import threading
import random
from math import factorial
from sympy import isprime


class FileNumberProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.primes_path = file_path.replace('.json', '_primes.json')
        self.fact_path = file_path.replace('.json', '_factorials.json')
        self.lock = threading.Lock()
        self.data_ready = threading.Event()

    def fill_numbers(self, count=100):
        numbers = [random.randint(1, 100) for _ in range(count)]
        with self.lock:
            with open(self.file_path, 'w') as file:
                json.dump(numbers, file)
        self.data_ready.set()

    def find_primes(self):
        self.data_ready.wait()
        with self.lock:
            with open(self.file_path, 'r') as file:
                numbers = json.load(file)
        primes = [num for num in numbers if isprime(num)]
        with open(self.primes_path, 'w') as file:
            json.dump(primes, file)
        print(f"Знайдено {len(primes)} Простих чисел.")

    def calculate_factorials(self):
        self.data_ready.wait()
        with self.lock:
            with open(self.file_path, 'r') as file:
                numbers = json.load(file)
        factorials = {num: factorial(num) for num in numbers}
        with open(self.fact_path, 'w') as file:
            json.dump(factorials, file)
        print(f"Підраховано факторіал для {len(factorials)} чисел.")

    def run(self):
        t1 = threading.Thread(target=self.fill_numbers)
        t2 = threading.Thread(target=self.find_primes)
        t3 = threading.Thread(target=self.calculate_factorials)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()


if __name__ == "__main__":
    processor = FileNumberProcessor('numbers.json')
    processor.run()
