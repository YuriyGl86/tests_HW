import unittest

import app
from app import *
from unittest.mock import patch
from parameterized import parameterized

FIXTURES = {'get_doc_owner_name': [('2207 876234', "Василий Гупкин"), ("10006", "Аристарх Павлов"),
                                   ('несуществующий номер', 'Нет такого документа')],
            'get_doc_shelf': [('2207 876234', "1"), ("10006", "2"),
                                   ('несуществующий номер', None)],
            'delete_doc': [("11111",)],
            }


class TestFunctions(unittest.TestCase):

    @parameterized.expand(FIXTURES['get_doc_owner_name'])
    def test_get_doc_owner_name(self, num, exp_result):
        with patch('builtins.input', return_value=num):
            result = get_doc_owner_name()
        self.assertEqual(result, exp_result)

    @parameterized.expand(FIXTURES['get_doc_shelf'])
    def test_get_doc_shelf(self, num, exp_result):
        with patch('builtins.input', return_value=num):
            result = get_doc_shelf()
        self.assertEqual(result, exp_result)

    @patch('app.get_new_doc', return_value=("11111", {"type": "passport", "number": "11111", "name": "Тестовый тест"}, '3'))
    def test_add_new_doc(self, func):
        add_new_doc()
        self.assertIn({"type": "passport", "number": "11111", "name": "Тестовый тест"}, app.documents)

    @parameterized.expand(FIXTURES['delete_doc'])
    def test_delete_doc(self, num):
        with patch('builtins.input', return_value=num):
            result = delete_doc()[1]
        self.assertTrue(result)
