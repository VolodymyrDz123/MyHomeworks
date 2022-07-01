from art import *
"""
Task 1. Напишіть функцію, що приймає один аргумант.
Функція має вивести на ектан тип цього аргумента (для визначення типу використайте type)
"""


def get_type(expected_value):
    print(text2art(str(type(expected_value)), font='block', chr_ignore=True))
    return type(expected_value)                               # return для тестування в test_homework5.py


"""
Task 2. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. 
Якщо перетворити не вдається функція має повернути 0 (флоатовий нуль).
"""


def into_float(value):
    try:
        return float(value)
    except ValueError:
        return 0.0
    except TypeError:
        return 0.0


"""
Task 3. Напишіть функцію, що приймає два аргументи. Функція повинна
якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
у будь-якому іншому випадку повернути кортеж з цих аргументів
"""


def type_actions(first_val, second_val):
    if (type(first_val) == int or type(first_val) == float) and (type(second_val) == int or type(second_val) == float):
        return first_val - second_val
    elif type(first_val) == str and type(second_val) == str:
        return first_val + second_val
    elif type(first_val) == str and type(second_val) != str:
        return {first_val: second_val}
    else:
        return first_val, second_val
