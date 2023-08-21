import unittest
from unittest.mock import patch
import os

from phonebook.editor import add_value


class TestPhonebookFunctions(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {"Фамилия": "Иванов", "Имя": "Иван", "Отчество": "Иванович", "Организация": "XYZ Corp",
             "Рабочий телефон": "12345", "Личный телефон": "67890"},
            {"Фамилия": "Петров", "Имя": "Петр", "Отчество": "Петрович", "Организация": "ABC Corp",
             "Рабочий телефон": "54321", "Личный телефон": "09876"}
        ]

    def test_load_phonebook(self):
        with open('test_phonebook.csv', 'w') as file:
            file.write('Фамилия,Имя,Отчество,Организация,Рабочий телефон,Личный телефон\n')
            for entry in self.sample_data:
                file.write(','.join(entry.values()) + '\n')

        phonebook = load_phonebook('test_phonebook.csv')
        os.remove('test_phonebook.csv')
        self.assertEqual(phonebook, self.sample_data)

    def test_save_phonebook(self):
        save_phonebook('test_phonebook_save.csv', self.sample_data)
        with open('test_phonebook_save.csv', 'r') as file:
            lines = file.readlines()

        os.remove('test_phonebook_save.csv')
        headers = lines[0].strip().split(',')
        self.assertEqual(headers, ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон'])

        for i, line in enumerate(lines[1:]):
            self.assertEqual(dict(zip(headers, line.strip().split(','))), self.sample_data[i])

    @patch('builtins.input', side_effect=["Тестов", "Тест", "Тестович", "Test Corp", "11111", "22222"])
    def test_add_value(self, mock_input):
        phonebook = []
        add_value(phonebook)
        self.assertEqual(phonebook[0]['Фамилия'], "Тестов")


if __name__ == "__main__":
    unittest.main()
