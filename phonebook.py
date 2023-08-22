import os

from pyfiglet import Figlet

PAGE_SIZE: int = 10

class Phonebook:
    """Вся логика работы телефонной книги."""
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.entries = []

    def load_entries(self) -> None:
        """Загрузка контактов из файла по указанному пути."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    entry_data = line.strip().split(';')
                    self.entries.append(entry_data)

    def save_entries(self) -> None:
        """Сохранение информации в файле."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            for entry in self.entries:
                file.write(';'.join(entry) + '\n')

    def display_entries(self, PAGE_SIZE: int) -> None:
        """Постраничный вывод всех записей."""
        for i, entry in enumerate(self.entries, start=1):
            contact_info = (
            f'\nКонтакт №{i}:\n'
            f'Фамилия: {entry[0]}\n'
            f'Имя: {entry[1]}\n'
            f'Отчество: {entry[2]}\n'
            f'Организация: {entry[3]}\n'
            f'Рабочий телефон: {entry[4]}\n'
            f'Личный телефон: {entry[5]}'
        )
            print(contact_info)
            if i % PAGE_SIZE == 0 or i == len(self.entries):
                input('\nНажмите Enter чтобы перелистнуть страницу...\n')

    def add_entry(self) -> None:
        """Добавление новой записи в телефонную книгу."""
        last_name = input('\nВведите фамилию: ')
        if not last_name.isalpha():
            raise ValueError(
                'Недопустимый формат фамилии. Используйте только буквы алфавита.'
            )
        first_name = input('Введите имя: ')
        if not first_name.isalpha():
            raise ValueError(
                'Недопустимый формат имени. Используйте только буквы алфавита.'
            )
        middle_name = input('Введите отчество: ')
        if not middle_name.isalpha():
            raise ValueError(
                'Недопустимый формат отчества. Используйте только буквы алфавита.'
            )
        organization = input('Введите название организации: ')
        if not organization.isalpha():
            raise ValueError(
                'Недопустимый формат названия. Используйте только буквы алфавита.'
            )
        work_phone = input('Введите рабочий номер телефона: ')
        if not work_phone.isdigit():
            raise ValueError(
                'Недопустимый формат рабочего телефона. Используйте только цифры.'
            )
        personal_phone = input('Введите личный номер телефона: ')
        if not personal_phone.isdigit():
            raise ValueError(
                'Недопустимый формат личного телефона. Используйте только цифры.'
            )
        self.entries.append(
            [last_name, first_name, middle_name, organization, work_phone, personal_phone]
        )
        if self.entries != []:
            self.save_entries()
            print('Контакт успешно добавлен!\n')

    def edit_entry(self) -> None:
        """Изменение выбранного контакта."""
        index = input('Введите номер контакта для его изменения: ')
        if not index.isdigit():
            raise ValueError('Неверный ввод: такого контакта не существует.')
        index = int(index)
        if 1 <= index <= len(self.entries):
            entry = self.entries[index - 1]
            contact_info = (
                f'\nИзменение контакта №{index}:\n'
                f'1. Фамилия: {entry[0]}\n'
                f'2. Имя: {entry[1]}\n'
                f'3. Отчество: {entry[2]}\n'
                f'4. Организация: {entry[3]}\n'
                f'5. Рабочий телефон: {entry[4]}\n'
                f'6. Личный телефон: {entry[5]}'
            )
            print(contact_info)
            field = input('Введите цифру поля для его редактирования: ')
            if not field.isdigit():
                raise ValueError('Неверный ввод: выберите число от 1 до 6')
            field = int(field)
            if 1 <= field <= 4:
                new_value = input('Введите новое значение: ')
                if not new_value.isalpha():
                    raise ValueError(
                        'Недопустимый формат. Используйте только буквы алфавита.'
                    )
                entry[field - 1] = new_value
                self.save_entries()
                print(f'Контакт успешно изменен! Поле {field}: {new_value}\n')
            elif 5 <= field <= 6:
                new_value = input('Введите новое значение: ')
                if not new_value.isdigit():
                    raise ValueError(
                        'Недопустимый формат. Используйте только цифры.'
                    )
                entry[field - 1] = new_value
                self.save_entries()
                print(f'Контакт успешно изменен! Поле {field}: {new_value}\n')
            else:
                print('Неверный номер поля.')
        else:
            print('Неверный номер контакта. Проверьте еще раз!')

    def search_entries(self) -> None:
        """Поиск среди контактов по указанному значению."""
        search_terms = []
        results = []
        while True:
            term = input('\nВведите поисковый запрос: ')
            field = input('Введите номер поля для поиска (1-6): ')
            search_terms.append((term, int(field) - 1))
            cont = input(
                'Хотите добавить еще один параметр для поиска? (yes/no): '
            )
            if cont.lower() != 'yes':
                break
        for entry in self.entries:
            if all(term.lower() in entry[field].lower() for term, field in search_terms):
                results.append(entry)
        if results:
            print('\nРезультаты поиска:')
            for i, entry in enumerate(results, start=1):
                contact_info = (
                f'\nКонтакт №{i}:\n'
                f'Фамилия: {entry[0]}\n'
                f'Имя: {entry[1]}\n'
                f'Отчество: {entry[2]}\n'
                f'Организация: {entry[3]}\n'
                f'Рабочий номер: {entry[4]}\n'
                f'Личный номер: {entry[5]}'
                )
                print(contact_info)
        else:
            print('\nПо запросу ничего не найдено.\n')

    def run_phonebook(self) -> None:
        """Запуск телефонной книги."""
        menu = {
            1: self.display_entries,
            2: self.add_entry,
            3: self.edit_entry,
            4: self.search_entries
        }

        while True:
            def animation():
                text = Figlet(font="banner", width=80).renderText("PHONE BOOK")
                print(text)
            animation()
            menu_text = (
            '\nДобро пожаловать в меню!\n\n'
            '1. Показать контакты\n'
            '2. Добавить контакт\n'
            '3. Изменить контакт\n'
            '4. Найти контакт\n'
            '5. Выход\n'
            )
            print(menu_text)
            try:
                choice = input('Введите (1-5): ')
                if not choice.isdigit():
                    raise ValueError('Неверный ввод: выберите число от 1 до 5')
                choice = int(choice)
                if 1 <= choice <= 4:
                    menu_function = menu.get(choice)
                    if choice == 1:
                        menu_function(PAGE_SIZE)
                    else:
                        menu_function()
                elif choice == 5:
                    print('Телефонный справочник закрыт. До скорого!')
                    break
                else:
                    print('\nТакой опции нет. Пожалуйста, выберите доступную (от 1 до 5).')
            except ValueError as e:
                print(f'Ошибка: {e}\n')


def main() -> None:
    """Старт программы. Загрузка данных и запуск работы телефонной книги."""
    phonebook = Phonebook('phonebook.txt')
    phonebook.load_entries()
    phonebook.run_phonebook()

if __name__ == "__main__":
    main()