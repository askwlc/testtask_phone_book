def not_empty(s):
    """Проверяет что значение не пустое."""
    return bool(s)

def is_number(s):
    """Проверяет что занчение число."""
    return s.isdigit()

def valid_input(entry, valid_func):
    """Функция проверки валидности ввода данных."""
    value = input(entry).strip()
    while not valid_func(value):
        print('Значение не может быть пустым. В номерах телефонов должны быть цифры.')
        value = input(entry).strip()
    return value
