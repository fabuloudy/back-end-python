
import unittest
from ti import TicTacGame
import numpy as np
class TestWinner(unittest.TestCase):
    def setUp(self):
        self.game1 = TicTacGame()
        self.game2 = TicTacGame()
        self.game3 = TicTacGame()
        self.game4 = TicTacGame()
        self.game5 = TicTacGame()
        self.game6 = TicTacGame()
        self.game7 = TicTacGame()
        self.game8 = TicTacGame()
        self.game9 = TicTacGame()
        self.game10 = TicTacGame()
        self.game11 = TicTacGame()
        self.game12 = TicTacGame()
        self.game13 = TicTacGame()
        self.game14 = TicTacGame()
        self.game15 = TicTacGame()
        self.game16 = TicTacGame()
        self.game1.config = ["X","2","3","4","X","6","7","8","X"]
        self.game2.config = ["O","2","3","4","O","6","7","8","O"]
        self.game3.config = ["1","2","X","4","X","6","X","8","9"]
        self.game4.config = ["1","2","O","4","O","6","O","8","9"]
        self.game5.config = ["X","X","X","4","5","6","7","8","9"]
        self.game6.config = ["O","O","O","4","5","6","7","8","9"]
        self.game7.config = ["1","2","3","X","X","X","7","8","9"]
        self.game8.config = ["1","2","3","O","O","O","7","8","9"]
        self.game9.config = ["1","2","3","4","5","6","X","X","X"]
        self.game10.config = ["1","2","3","4","5","6","O","O","O"]
        self.game11.config = ["X","2","3","X","5","6","X","8","9"]
        self.game12.config = ["O","2","3","O","5","6","O","8","9"]
        self.game13.config = ["1","X","3","4","X","6","7","X","9"]
        self.game14.config = ["1","O","3","4","O","6","O","O","O"]
        self.game15.config = ["1","2","X","4","5","X","7","8","X"]
        self.game16.config = ["1","2","O","4","5","O","7","8","O"]
        self.game1.turn = "X"
        self.game2.turn = "O"
        self.game3.turn = "FX"
        self.game4.turn = "FO"
        self.game5.turn = "FD"
        self.game6.turn = "X"

    def test_check_winner(self):
        self.assertTrue(self.game1.check_winner(), "Но тут есть победилеть1...")
        self.assertTrue(self.game2.check_winner(), "Но тут есть победилеть2...")
        self.assertTrue(self.game3.check_winner(), "Но тут есть победилеть3...")
        self.assertTrue(self.game4.check_winner(), "Но тут есть победилеть4...")
        self.assertTrue(self.game5.check_winner(), "Но тут есть победилеть5...")
        self.assertTrue(self.game6.check_winner(), "Но тут есть победилеть6...")
        self.assertTrue(self.game7.check_winner(), "Но тут есть победилеть7...")
        self.assertTrue(self.game8.check_winner(), "Но тут есть победилеть8...")
        self.assertTrue(self.game9.check_winner(), "Но тут есть победилеть9...")
        self.assertTrue(self.game10.check_winner(), "Но тут есть победилеть10...")
        self.assertTrue(self.game11.check_winner(), "Но тут есть победилеть11...")
        self.assertTrue(self.game12.check_winner(), "Но тут есть победилеть12...")
        self.assertTrue(self.game13.check_winner(), "Но тут есть победилеть13...")
        self.assertTrue(self.game14.check_winner(), "Но тут есть победилеть14...")
        self.assertTrue(self.game15.check_winner(), "Но тут есть победилеть15...")
        self.assertTrue(self.game16.check_winner(), "Но тут есть победилеть16...")

    def test_validate_input(self):
        self.assertTrue(self.game1.validate_input("4"),"А тут что не так?")
        self.assertFalse(self.game1.validate_input("5"),"Но ведь клетка занята")
        self.assertFalse(self.game1.validate_input("йцу"), "Это что команда?")
        self.assertFalse(self.game1.validate_input("10"), "Перебор...")
        self.assertFalse(self.game1.validate_input("-4"),"ye")

    def test_do_move(self):
        self.game1.do_move("0")
        self.assertEqual(self.game1.turn,"FO")
        self.game2.do_move("2")
        self.assertEqual(self.game2.config[1],"O")
        self.game6.do_move("3")
        self.assertEqual(self.game6.config[2],"X")

    def test_analyze_turn(self):
        self.assertTrue(self.game1.analyze_turn())
        self.assertTrue(self.game2.analyze_turn())
        self.assertFalse(self.game3.analyze_turn())
        self.assertFalse(self.game4.analyze_turn())
        self.assertFalse(self.game5.analyze_turn())

    def test_change_turn(self):
        self.game1.change_turn()
        self.assertEqual(self.game1.turn,"O")
        self.game2.change_turn()
        self.assertEqual(self.game2.turn,"X")
        self.game3.change_turn()
        self.assertEqual(self.game3.turn,"FX")

if __name__ == '__main__':
    unittest.main()
