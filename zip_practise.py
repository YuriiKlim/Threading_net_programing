# Є словник з друзями, де ключ – людина, а значення –
# список друзів. Користувач вводить імена двох людей,
# які є друзями, повторює це певну кількість разів,
# після чого дані зберігаються у файл.
# Завантажте дані назад та виведіть на екран.
import json


def add_friends(friends_dict):
    print("Введіть імена у форматі 'ім'я: друг1, друг2, ...'")
    while True:
        input_data = input("Введіть ім'я людини та її друзів або 'enter' для завершення: ")
        if input_data.lower() == '':
            break

        if ':' in input_data:
            person, friends_str = input_data.split(':', 1)
            friends = [friend.strip() for friend in friends_str.split(',')]
        else:
            print("Невірний формат вводу.")
            continue

        if person in friends_dict:
            friends_dict[person].update(friends)
        else:
            friends_dict[person] = set(friends)

        for friend in friends:
            if friend in friends_dict:
                friends_dict[friend].add(person)
            else:
                friends_dict[friend] = {person}


def save_data(friends_dict):
    with open("friends_data.json", "w") as file:
        json.dump({key: list(value) for key, value in friends_dict.items()}, file)


friends_dict = {}
add_friends(friends_dict)
save_data(friends_dict)


def load_and_display_data():
    try:
        with open("friends_data.json", "r") as file:
            friends_dict = json.load(file)
            for person, friends in friends_dict.items():
                print(f"{person}: {', '.join(friends)}")
    except FileNotFoundError:
        print("Файл не знайдено.")


load_and_display_data()



