from dice_class import Dice


class Game(object):
    def __init__(self):
        self.dices = list(map(lambda a: Dice(), range(3)))

    def throw(self, first, second, third):
        self.dices[0].set_scores(first)
        self.dices[1].set_scores(second)
        self.dices[2].set_scores(third)

        scores = [d.scores for d in self.dices]

        if scores.count(scores[0]) == 3:
            return scores[0] * 100
        elif scores.count(scores[0]) == 2:
            return scores[0] * 10
        elif scores.count(scores[1]) == 2:
            return scores[1] * 10

        return sum(scores)


