# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.
import threading


def search_word_in_file(path, word):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            count = content.count(word)
            if count > 0:
                print(f"Слово '{word}' знайдено {count} разів у файлі.")
            else:
                print(f"Слово '{word}' не знайдено у файлі.")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")


def main():
    path = input("Введіть шлях до файлу: ")
    word = input("Введіть слово для пошуку: ")
    search_thread = threading.Thread(target=search_word_in_file, args=(path, word))
    search_thread.start()
    search_thread.join()


if __name__ == "__main__":
    main()
