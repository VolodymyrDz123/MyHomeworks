import pytest
import dice_game
import custom_exceptions


@pytest.fixture()
def game_creating():
    return dice_game.Game()


@pytest.mark.parametrize("first, second, third, scores", [(4, 5, 6, 15),
                                                          (3, 3, 3, 300),
                                                          (5, 5, 6, 50),
                                                          (6, 2, 2, 20)])
def test_all_rules(game_creating, first, second, third, scores):
    assert game_creating.throw(first, second, third) == scores


@pytest.mark.parametrize("first, second, third, exception", [(5, 0, 3, custom_exceptions.DiceZeroError),
                                                             (3, -1, 6, custom_exceptions.DiceNegativeError),
                                                             (4, 4, 7, custom_exceptions.DiceTooBigError),
                                                             (6, "s", 2, custom_exceptions.DiceNotIntError)])
def test_zero_error(game_creating, first, second, third, exception):
    with pytest.raises(exception):
        game_creating.throw(first, second, third)
