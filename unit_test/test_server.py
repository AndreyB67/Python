"""Unit-тесты сервера"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server import process_client_message


class TestServer(unittest.TestCase):
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}

    def test_ok_check(self):
#Тест корректности запроса
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

    def test_no_action(self):
#Тест на наличие ошибки нет действия
        self.assertEqual(process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
#Тест на наличие ошибки неизвестное действие
        self.assertEqual(process_client_message(
            {ACTION: 'Hacker attack', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_time(self):
#Тест на наличие ошибки запрос не содержит штампа времени
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_user(self):
#Тест на наличие ошибки - нет пользователя
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
#Тест на наличие ошибки идентификации пользователя
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Ivanov'}}), self.err_dict)

if __name__ == '__main__':
    unittest.main()
