"""TicTac Game by @julwelier"""


class TicTacGame:
    '''Main Game Class'''
    turn = "X"

    def __init__(self):
        self.config = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def show_board(self):
        '''func for show'''
        conf = self.config
        print("|{}|{}|{}|".format(conf[0], conf[1], conf[2]))
        print("|{}|{}|{}|".format(conf[3], conf[4], conf[5]))
        print("|{}|{}|{}|".format(conf[6], conf[7], conf[8]))

    def change_turn(self):
        '''func for changing turn'''
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"

    def do_move(self, move):
        '''func for moving'''
        if move == "0":  # игрок сдался
            if self.turn == "X":
                self.turn = "FO"
            else:
                self.turn = "FX"

        elif self.turn == "X":
            self.config[int(move)-1] = "X"
        elif self.turn == "O":
            self.config[int(move)-1] = "O"

    def validate_input(self, move):
        '''func for checking input'''
        correct_input = True
        if move.isdigit() and int(move) // 10 == 0 and int(move) != 0:
            if (self.config[int(move)-1] == "X" or
                    self.config[int(move)-1] == "O"):
                print("Поле уже занято! Сделайте другой ход.")
                correct_input = False
        elif move != "0":
            print("Неверный формат ввода! Попробуйте снова!")
            correct_input = False
        return correct_input

    def analyze_turn(self):
        '''function for analyzing current turn'''
        self.show_board()
        continue_game = True
        if self.turn == "X":
            print("Ходят крестики!")
        elif self.turn == "O":
            print("Ходят нолики!")
        elif self.turn == "FO":
            print("Победили нолики!")
            continue_game = False
        elif self.turn == "FX":
            print("Победили крестики!")
            continue_game = False
        else:
            print("Ничья!")
            continue_game = False
        return continue_game

    def play_game(self):
        '''func for start'''
        correct_input = bool()
        while self.analyze_turn():
            correct_input = False
            move = str()
            while correct_input is not True:
                move = input('Введите число от 1 до 9: ')
                correct_input = self.validate_input(move)

            self.do_move(move)
            if self.check_winner() is False:
                self.change_turn()
            else:
                if self.turn != "FX" and self.turn != "FO":
                    self.turn = "F" + self.turn

    def check_winner(self):
        '''Function for checking winner'''
        if self.turn[0] == "F":
            return True
        conf = self.config
        win_position = [
                        (0, 4, 8), (2, 4, 6),
                        (0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8)
                        ]
        for pos in win_position:
            if conf[pos[0]] == conf[pos[1]] == conf[pos[2]]:
                return True
        unfilled = False
        for i in range(9):
            if str(i+1) == conf[i]:
                unfilled = True
        if unfilled is False:
            self.turn = "D"
            return True
        return False


if __name__ == '__main__':
    print("""Формат хода: 1,2...,9
Выбираете ячейку, на которую хотите поставить фигуру
Если хотите сдаться - введите 0""")
    game = TicTacGame()
    game.play_game()
