"""Программа для игры в крестики-нолики"""
board = list(range(1, 10))


class TicTacGame:
    """Класс для игры в крестики-нолики"""

    def show_board(self):
        """Метод отрисовки поля"""
        for i in range(3):
            print("-" * 10)
            print(board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3])
        print("-" * 10)

    def validate_input(self, player, num_field):
        """Проверка корректности вводимого поля"""
        try:
            if int(num_field) < 1:
                tip = "Некорретный ввод данных - введено число меньше 1!"

            elif "X" == board[int(num_field) - 1] or "O" == board[int(num_field) - 1]:
                tip = "Некорретный ввод данных - это поле занято!"

            else:
                board[int(num_field) - 1] = player
                game.show_board()
                tip = True
                return tip
        except ValueError:
            tip = "Некорретный ввод данных - введено не число!"

        except IndexError:
            tip = "Некорретный ввод данных - введено число больше 9!"

        if tip is not True:
            print(tip)
            return tip
        return None

    def start_game(self):
        """Старт игры"""
        count = 1
        game.show_board()
        while count != 10:

            if count % 2 == 1:
                player = "X"
            else:
                player = "O"
            while game.validate_input(player, input(f'Введите номер поля {player}: ')) is not True:
                print()
            count += 1
            if count > 5:
                if game.check_winner(player, board) == f'Победа игрока {player}':
                    break
        else:
            print("Ничья!")

    def check_winner(self, player, board):
        """Проверка кто победил"""
        winner_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]
        for i in winner_board:
            if board[i[0]] == board[i[1]] == board[i[2]]:
                print(f'Победа игрока {player}')
                return f'Победа игрока {player}'
        return "Пока победителя нет"


game = TicTacGame()

if __name__ == '__main__':
    game.start_game()
    game.show_board()
