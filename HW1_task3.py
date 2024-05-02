# Завдання 3
# Користувач вводить з клавіатури шлях до існуючої та
# до нової директорії. Після чого запускається потік, який має
# скопіювати вміст директорії у нове місце. Збережіть структуру
# директорії. Виведіть статистику виконаних операцій на екран.
import os
import shutil
import threading


def copy_directory(src, dst):
    try:
        os.makedirs(dst, exist_ok=True)
        print(f"Копіювання файлів з {src} до {dst}")
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copy_directory(s, d)
            else:
                shutil.copy2(s, d)
                print(f"'{item}' скопійовано з '{src}' до '{dst}'")
    except Exception as e:
        print(f"Помилка при копіюванні: {e}")


def main():
    source = input("Введіть шлях до існуючої директорії: ")
    destination = input("Введіть шлях до нової директорії: ")

    if os.path.isdir(source):
        thread = threading.Thread(target=copy_directory, args=(source, destination))
        thread.start()
        thread.join()
        print("Копіювання завершено.")
    else:
        print("Вказано невірний шлях до директорії.")


if __name__ == "__main__":
    main()
