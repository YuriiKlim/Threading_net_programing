# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.
import threading


def find_sum(numbers):
    sum_value = sum(numbers)
    print(f"Сумма: {sum_value}")


def find_mean(numbers):
    sum_value = sum(numbers)
    mean_value = sum_value / len(numbers)
    print(f"Середнє: {mean_value}")


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
        max_thread = threading.Thread(target=find_sum, args=(numbers,))
        min_thread = threading.Thread(target=find_mean, args=(numbers,))

        max_thread.start()
        min_thread.start()

        max_thread.join()
        min_thread.join()
    else:
        print("Список пустий. Немає даних для обробки.")


if __name__ == "__main__":
    main()