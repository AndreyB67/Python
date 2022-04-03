import sys
import os
import unittest
import json
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING
from common.utils import get_message, send_message


class TestSocket:
# Тестовый класс для тестирования отправки и получения,
# при создании требует словарь, который будет прогонятся
# через тестовую функцию

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        # Тестовая функция отправки
        json_test_message = json.dumps(self.test_dict)
        # кодирует сообщение
        self.encoded_message = json_test_message.encode(ENCODING)
        # сохраняем что должно было отправлено в сокет
        self.received_message = message_to_send

    def recv(self, max_len):
        # Получаем данные из сокета
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 111111.111111,
        USER: {
            ACCOUNT_NAME: 'test_utils'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_send_message(self):
        # экземпляр тестового словаря
        test_socket = TestSocket(self.test_dict_send)
        # вызов тестируемой функции
        send_message(test_socket, self.test_dict_send)
        # проверка корретности кодирования словаря.
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)


    def test_send_message_temp(self):
        # экземпляр тестового словаря
        test_socket = TestSocket(self.test_dict_send)
        # вызов тестируемой функции
        send_message(test_socket, self.test_dict_send)
        # проверим генерацию исключения
        self.assertRaises(TypeError, send_message, test_socket, "wrong_dictionary")

    def test_get_message_corr(self):
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        test_sock_err = TestSocket(self.test_dict_recv_err)
        # тест корректной расшифровки корректного словаря
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

    def test_get_message_uncorr(self):
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        test_sock_err = TestSocket(self.test_dict_recv_err)
        # тест отсутствия некорректного словаря
        self.assertNotEqual(get_message(test_sock_err), self.test_dict_recv_ok)


    def test_get_message_error(self):
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        test_sock_err = TestSocket(self.test_dict_recv_err)
        # тест корректной расшифровки ошибочного словаря
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()
