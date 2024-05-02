# Завдання 4
# Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку. Після чого запускаються два
# потоки. Перший потік має знайти файли з потрібним словом
# і злити їх вміст в один файл. Другий потік очікує на завершення роботи першого потоку і проводить виключення усіх
# заборонених слів (список цих слів потрібно зчитати з файлу
# із забороненими словами) з отриманого файлу. Виведіть статистику виконаних операцій на екран.
import threading
import os


def find_and_merge_files(directory, search_word, output_file):
    merged_content = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if search_word in content:
                    merged_content += content + "\n"
            except Exception as e:
                print(f"Не вдалося прочитати файл {file}: {e}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(merged_content)
    print(f"Файли зі словом '{search_word}' були злиті в {output_file}")


def filter_banned_words(output_file, banned_words_file):
    with open(banned_words_file, 'r') as f:
        banned_words = f.read().split()
    with open(output_file, 'r') as f:
        content = f.read()
    for word in banned_words:
        content = content.replace(word, ""*len(word))
    with open(output_file, 'w') as f:
        f.write(content)
    print(f"Заборонені слова були видалені з {output_file}")


def main():
    directory = input("Введіть шлях до директорії: ")
    search_word = input("Введіть слово для пошуку: ")
    output_file = "merged_output.txt"
    banned_words_file = "banned_words.txt"

    thread1 = threading.Thread(target=find_and_merge_files, args=(directory, search_word, output_file))
    thread2 = threading.Thread(target=filter_banned_words, args=(output_file, banned_words_file))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()


if __name__ == "__main__":
    main()
