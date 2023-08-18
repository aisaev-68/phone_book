import csv

DATA_FILE = "data/test_data.csv"


def load_phonebook():
    """
    Функция для чтения файла.
    :return:
    """
    try:
        with open(DATA_FILE, "r", newline="") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def save_phonebook(phonebook):
    """
    Функция для сохранения файла.
    :param phonebook:
    :return:
    """
    fieldnames = ["surname", "first_name", "middle_name", "organization", "work_phone", "personal_phone", "address", "email"]
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(phonebook)


def display_entries(entries, page_num, entries_per_page):
    """
    Функция для просмотра справочника
    :param entries:
    :param page_num:
    :param entries_per_page:
    :return:
    """
    start_idx = (page_num - 1) * entries_per_page
    end_idx = start_idx + entries_per_page
    for idx, entry in enumerate(entries[start_idx:end_idx], start=start_idx + 1):
        print(f"Введите {idx}:")
        for field, value in entry.items():
            print(f"{field.capitalize()}: {value}")
        print("=" * 40)


def add_or_edit_entry(edit=False, entry_idx=None):
    """
    Функция для добавления и редактирования записи.
    :param edit:
    :param entry_idx:
    :return:
    """
    entry = {
        field: input(f"Введите {field.replace('_', ' ')}: ") for field in fieldnames
    }
    if edit:
        phonebook[entry_idx] = entry
        print("Запись успешно изменена!")
    else:
        phonebook.append(entry)
        print("Запись успешно добавлена!")
    save_phonebook(phonebook)


def search_entries():
    """
    Функция поиска записей по нескольким характеристикам,кроме email.

    :return:
    """
    search_term = input("Введите поисковый запрос: ").lower()
    search_results = [
        entry for entry in phonebook
        if any(search_term in value.lower() for value in entry.values())
    ]
    if search_results:
        display_entries(search_results, 1, len(search_results))
    else:
        print("Не найдено подходящих записей.")


if __name__ == "__main__":
    phonebook = load_phonebook()
    fieldnames = phonebook[0].keys() if phonebook else []

    while True:
        print("Меню телефонной книги:")
        print("1. Показать записи")
        print("2. Добавить новую запись")
        print("3. Изменить запись")
        print("4. Поиск записей")
        print("5. Выход")
        choice = input("Введите свой выбор: ")

        if choice == "1":
            page_num = int(input("Введите номер страницы: "))
            entries_per_page = 5
            display_entries(phonebook, page_num, entries_per_page)
        elif choice == "2":
            add_or_edit_entry()
        elif choice == "3":
            entry_idx = int(input("Введите номер записи для редактирования: ")) - 1
            if 0 <= entry_idx < len(phonebook):
                add_or_edit_entry(edit=True, entry_idx=entry_idx)
            else:
                print("Неверный номер записи.")
        elif choice == "4":
            search_entries()
        elif choice == "5":
            save_phonebook(phonebook)
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите еще раз.")
