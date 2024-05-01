# Завдання 1
# При старті додатку запускаються три потоки. Перший
# потік заповнює список випадковими числами. Два інші потоки
# очікують на заповнення. Коли перелік заповнений, обидва
# потоки запускаються. Перший потік знаходить суму елементів
# списку, другий потік знаходить середнє арифметичне значення
# у списку. Отриманий список, сума та середнє арифметичне
# виводяться на екран.
import threading
import random


class NumberListProcessor:
    def __init__(self, size=100):
        self.size = size
        self.numbers = []
        self.sum_done = threading.Event()
        self.mean_done = threading.Event()

    def fill_numbers(self):
        for _ in range(self.size):
            self.numbers.append(random.randint(1, 100))
        self.sum_done.set()
        self.mean_done.set()

    def calculate_sum(self):
        self.sum_done.wait()
        total_sum = sum(self.numbers)
        print(f"Сума: {total_sum}")

    def calculate_mean(self):
        self.mean_done.wait()
        if self.numbers:
            mean_value = sum(self.numbers) / len(self.numbers)
            print(f"Середнє: {mean_value:.2f}")

    def run(self):
        filler_thread = threading.Thread(target=self.fill_numbers)
        sum_thread = threading.Thread(target=self.calculate_sum)
        mean_thread = threading.Thread(target=self.calculate_mean)

        filler_thread.start()
        sum_thread.start()
        mean_thread.start()

        filler_thread.join()
        sum_thread.join()
        mean_thread.join()

        print(f"Згенерований список чисел: {self.numbers}")


processor = NumberListProcessor(size=10)
processor.run()


