from tasks_homework5 import get_type, into_float, type_actions
import pytest


# Test for task 1
@pytest.mark.parametrize("text, print_type", [(1, int),
                                              (True, bool),
                                              (2.3, float),
                                              ("asd", str),
                                              ([1, 2, "asd"], list),
                                              ((1, 2, "as"), tuple),
                                              ({1: 2, "asd": 2.4}, dict),
                                              ({12, "sad", 42}, set)])
def test_get_type(text, print_type):
    assert get_type(text) == print_type


# Test for task 2
@pytest.mark.parametrize("value, expected_float", [(1, 1.0),
                                                   (2.3, 2.3),
                                                   ("6.6", 6.6),
                                                   ("3", 3.0),
                                                   ("asd", 0.0),
                                                   (True, 1.0),
                                                   (False, 0.0),
                                                   (None, 0.0),
                                                   ([1, 2, "asd"], 0.0),
                                                   ((1, 2, "as"), 0.0),
                                                   ({1: 2, "asd": 2.4}, 0.0),
                                                   ({12, "sad", 42}, 0.0)])
def test_into_float(value, expected_float):
    assert into_float(value) == expected_float


# Test for task 3
@pytest.mark.parametrize("first_data, second_data, expected_result", [(10, 4, 6),
                                                                      (2.3, 2.3, 0.0),
                                                                      (6.6, 1, 5.6),
                                                                      ("3", "3.0", "33.0"),
                                                                      ("Hello ", "World!", "Hello World!"),
                                                                      ("True", 0.0, {"True": 0.0}),
                                                                      ("str", True, {"str": True}),
                                                                      ("MyNone", 46, {"MyNone": 46}),
                                                                      ([1, 2, "asd"], 0.0, ([1, 2, "asd"], 0.0)),
                                                                      ((1, 2, "as"), "saf", ((1, 2, "as"), "saf")),
                                                                      (564, "UI123", (564, "UI123"))])
def test_type_actions(first_data, second_data, expected_result):
    assert type_actions(first_data, second_data) == expected_result
