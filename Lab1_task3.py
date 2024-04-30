# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.
import json
import threading


# numbers = list(range(1, 1000001))
#
# with open('numbers.json', 'w') as file:
#     json.dump(numbers, file)


def save_even_numbers(numbers, filename="even_numbers.json"):
    even_numbers = [num for num in numbers if num % 2 == 0]
    with open(filename, 'w') as file:
        json.dump(even_numbers, file)
    print(f"Кількість парних чисел: {len(even_numbers)}")


def save_odd_numbers(numbers, filename="odd_numbers.json"):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    with open(filename, 'w') as file:
        json.dump(odd_numbers, file)
    print(f"Кількість непарних чисел: {len(odd_numbers)}")


def main():
    filepath = "numbers.json"
    try:
        with open(filepath, 'r') as file:
            numbers = json.load(file)

        even_thread = threading.Thread(target=save_even_numbers, args=(numbers,))
        odd_thread = threading.Thread(target=save_odd_numbers, args=(numbers,))

        even_thread.start()
        odd_thread.start()

        even_thread.join()
        odd_thread.join()

    except FileNotFoundError:
        print("Файл не знайдено.")
    except json.JSONDecodeError:
        print("Помилка читання JSON.")


if __name__ == "__main__":
    main()
