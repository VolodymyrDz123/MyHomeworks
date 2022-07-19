"""
Розробити функцію, котра приймає колекцію та обʼєкт функції, що приймає один аргумент.
Певернути колекцію, кожен член якої є перетвореним членом вхідної колекції.

Нотатка. Обʼєкт функції, яку передаємо вказує на функцію,
котра приймає один аргумент. Не користуватися функціями map чи filter!!!
"""


def collect_func(your_list, your_func):
    result = []
    for every_value in your_list:
        result.append(your_func(every_value))
    return result


def multiple(value):
    return value * 2


list_example = [1, 2, 3, 4, 5]
print(collect_func(list_example, multiple))

