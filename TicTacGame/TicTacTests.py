"""Модуль для тестирования основных функций"""
from unittest import TestCase, main
from main import *


class TicTacGameTest(TestCase):

    def test_check_winner_X(self):
        board = ["X", "X", "X", 4, 5, 6, 7, 8]
        self.assertEqual(TicTacGame.check_winner(self, "X", board), f'Победа игрока X')

    def test_check_winner_O(self):
        board = [1, "X", "O", 4, "X", "O", "X", 8, "O"]
        self.assertEqual(TicTacGame.check_winner(self, "O", board), f'Победа игрока O')

    def test_check_winner_None(self):
        board = [1, "X", "O", 4, "X", "O", "X", 8, 9]
        self.assertEqual(TicTacGame.check_winner(self, "O", board), "Пока победителя нет")

    def test_validate_input_cor(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(TicTacGame.validate_input(self, "X", 1), True)

    def test_validate_input_0(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(TicTacGame.validate_input(self, "X", 0), "Некорретный ввод данных - введено число меньше 1!")

    def test_validate_input_10(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(TicTacGame.validate_input(self, "X", 10), "Некорретный ввод данных - введено число больше 9!")

    def test_validate_input_str(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(TicTacGame.validate_input(self, "X", "str"), "Некорретный ввод данных - введено не число!")

    def test_validate_input_z(self):
        board = ["X", 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(TicTacGame.validate_input(self, "O", 1), "Некорретный ввод данных - это поле занято!")


if __name__ == "__main__":
    main()
