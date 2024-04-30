# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
import threading


def find_max(numbers):
    max_value = max(numbers)
    print(f"Максимальне значення: {max_value}")


def find_min(numbers):
    min_value = min(numbers)
    print(f"Мінімальне значення: {min_value}")


def main():
    numbers = []
    while True:
        try:
            number = input("Введіть число (або натисніть Enter для завершення): ")
            if not number:
                break
            numbers.append(int(number))
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")

    if numbers:
        max_thread = threading.Thread(target=find_max, args=(numbers,))
        min_thread = threading.Thread(target=find_min, args=(numbers,))

        max_thread.start()
        min_thread.start()

        max_thread.join()
        min_thread.join()
    else:
        print("Список пустий. Немає даних для обробки.")


if __name__ == "__main__":
    main()
