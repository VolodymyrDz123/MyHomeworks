import custom_exceptions


class Dice(object):
    def __init__(self):
        self.__scores = 1

    @property
    def scores(self):
        return self.__scores

    def set_scores(self, num):
        if type(num) != int:
            raise custom_exceptions.DiceNotIntError
        if num == 0:
            raise custom_exceptions.DiceZeroError
        if num < 0:
            raise custom_exceptions.DiceNegativeError
        if num > 6:
            raise custom_exceptions.DiceTooBigError
        self.__scores = num
