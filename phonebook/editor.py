from .validation import is_number, not_empty, valid_input


def display_values(results):
    """Функция отформатированного отображения записей."""
    for value in results:
        for key, val in value.items():
            print(f"{key}: {val}")
        print('-' * 40)


def add_value(phonebook):
    """Добавление записей в телефонную книгу."""
    surname = valid_input("Введите Фамилию: ", not_empty)
    first_name = valid_input("Введите Имя: ", not_empty)
    patronymic = input("Введите Отчество: ")
    company = input("Введите название организации: ")
    work_phone = valid_input("Введите рабочий телефон: ", is_number)
    personal_phone = valid_input("Введите личный телефон: ", is_number)

    new_value = {
        'Фамилия': surname,
        'Имя': first_name,
        'Отчество': patronymic,
        'Организация': company,
        'Рабочий телефон': work_phone,
        'Личный телефон': personal_phone
    }

    phonebook.append(new_value)
    print('Записи успешно добавлены')


def list_values(phonebook, page_size=2):
    """Функция вывода записей постранично."""
    num_pages = len(phonebook) // page_size + (1 if len(phonebook) % page_size else 0)
    current_page = 0

    while True:
        start_index = current_page * page_size
        end_index = start_index + page_size
        display_values(phonebook[start_index:end_index])

        if num_pages == 1:
            break

        response = input(f'Введите номер страницы от 1 до {num_pages}, или "q" - для выхода: ')

        if response == 'q':
            break
        elif response.isdigit() and 1 <= int(response) <= num_pages:
            current_page = int(response) - 1
        else:
            print(f'Неверное значение. Введите номер страницы от 1 до {num_pages}, или "q" - для выхода.')
            continue


def search_value(phonebook):
    """Функция поиска записи в телефонной книге."""
    search_value = input('Введите Имя или Фамилию для поиска: ').strip().lower()
    results = [
        value for value in phonebook
        if search_value in value['Фамилия'].lower()
           or search_value in value['Имя'].lower()
    ]
    if not results:
        print('Запись не найдена')
    else:
        display_values(results)


def edit_value(phonebook):
    """Функция редактирования записи в телефонной книге."""
    search_surname = valid_input('Введите Фамилию, для редактирования записи: ', not_empty)
    values_to_edit = [value for value in phonebook if value['Фамилия'].lower() == search_surname.lower()]

    if not values_to_edit:
        return f'Нет записей с такой Фамилией.'

    for i, value in enumerate(values_to_edit):
        print(f'{i + 1}. {value["Фамилия"]} {value["Имя"]} {value["Отчество"]}')

    try:
        index = int(valid_input('Введите номер записи, для редактирования: ', is_number))
        value_edit = values_to_edit[index - 1]
    except (ValueError, IndexError):
        return f'Неверное значение индекса.'

    fields = ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']
    for i, f in enumerate(fields):
        print(f'{i + 1} - {f}')

    field_number = valid_input(f'Введите номер ячейки для редактирования: ',
                              lambda x: x.isdigit() and 1 <= int(x) <= len(fields))

    field = fields[int(field_number) - 1]
    new_value = input(f'Введите новое значение для поля {field}: ').strip()
    value_edit[field] = new_value

    print('Запись отредактирована.')
