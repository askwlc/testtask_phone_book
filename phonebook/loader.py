def load_phonebook(file):
    """Функция загрузки файла телефонной книги."""
    phonebook = []

    with open(file, 'r') as file:
        headers = file.readline().strip().split(',')

        for line in file:
            values = line.strip().split(',')
            values_dict = dict(zip(headers, values))
            phonebook.append(values_dict)

    return phonebook

def save_phonebook(file, phonebook):
    """Функция сохранения файла телефонной книги."""

    with open(file, 'w') as file:
        headers = ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']
        file.write(','.join(headers) + '\n')

        for value in phonebook:
            values = [value[header] for header in headers]
            file.write(','.join(values) + '\n')
