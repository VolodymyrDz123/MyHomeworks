import unittest
import dice_game
import custom_exceptions


class TestDice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.game = dice_game.Game()

    def test_default_dice(self):
        self.assertEqual(self.game.dices[0].scores, 1)

    def test_standard_game(self):
        self.assertEqual(self.game.throw(4, 5, 6), 15)

    def test_first_rule(self):
        self.assertEqual(self.game.throw(3, 3, 3), 300)

    def test_second_rule(self):
        self.assertEqual(self.game.throw(5, 5, 6), 50)

    def test_third_rule(self):
        self.assertEqual(self.game.throw(6, 2, 2), 20)

    def test_zero_error(self):
        with self.assertRaises(custom_exceptions.DiceZeroError):
            self.game.throw(5, 0, 3)

    def test_negatives_error(self):
        with self.assertRaises(custom_exceptions.DiceNegativeError):
            self.game.throw(5, -1, 6)

    def test_too_big_error(self):
        with self.assertRaises(custom_exceptions.DiceTooBigError):
            self.game.throw(4, 4, 7)

    def test_type_error(self):
        with self.assertRaises(custom_exceptions.DiceNotIntError):
            self.game.throw(3, "a", 3)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)