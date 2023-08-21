from editor import add_value, list_values, search_value, edit_value
from loader import save_phonebook, load_phonebook
from validation import valid_input, not_empty, is_number


def main(phonebook):
    """Функция интерфейс работы с телефонной книгой."""
    file = 'data/phonebook.csv'
    commands = {
        '1': {"action": "list", "function": list_values},
        '2': {"action": "search", "function": search_value},
        '3': {"action": "add", "function": add_value},
        '4': {"action": "edit", "function": edit_value},
        '5': {"action": "quit", "function": None}
    }

    while True:
        print('Доступные команды:')
        for key, value in commands.items():
            print(f'{key}. {value["action"]}')

        command_number = valid_input(
            'Введите номер команды: ',
            lambda x: not_empty(x) and is_number(x)
        )

        if command_number in commands:
            if commands[command_number]['action'] == 'quit':
                save_phonebook(file, phonebook)
                break
            else:
                commands[command_number]['function'](phonebook)
        else:
            print('Неверное значение, попробуйте ещё раз.')


if __name__ == '__main__':
    file = 'data/phonebook.csv'
    phonebook = load_phonebook(file)
    main(phonebook)
