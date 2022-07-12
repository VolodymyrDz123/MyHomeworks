"""
Hапишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:

Попросіть користувача ввести свсвій вік.
- якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
- якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
- якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
- якщо вік користувача складається з однакових цифр
(11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"

Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік

Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.

Наприклад :
"Тобі ж 5 років! Де твої батьки?"
"Вам 81 рік? Покажіть пенсійне посвідчення!"
"О, вам 33 роки! Який цікавий вік!"

Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг або тайпхінтінг.
Не забувайте що кожна функція має виконувати тільки одну завдання і про правила написання коду.
"""


def age_ending(years_old):
    """
    Function for determine the correct ending for the word "Рік"
    :param years_old: customer age
    :type: int
    :return: the word "Рік" with correct ending
    """
    str_years_old = str(years_old)
    if len(str_years_old) > 1 and str_years_old[-2] == "1":
        return "років"
    elif str_years_old.endswith("1"):
        return "рік"
    elif str_years_old.endswith("2") or str_years_old.endswith("3") or str_years_old.endswith("4"):
        return "роки"
    else:
        return "років"


def answer_generation(customer_age):
    """
    Function for generation a correct answer to a client
    :param customer_age: entered age
    :type: str
    :return: correct answer
    """
    try:
        int_customer_age = int(customer_age)
    except (ValueError, TypeError):
        print("Ваш вік має бути в цілих цифрах!")
    else:
        if int_customer_age <= 0:
            print("Ваш вік не може бути нуль або мінусове значення!")
        else:
            years = age_ending(int_customer_age)
            if customer_age.count(customer_age[0]) == len(customer_age) and len(customer_age) != 1:
                print(f"О, вам {int_customer_age} {years}! Який цікавий вік!")
            elif int_customer_age < 7:
                print(f"Тобі ж {int_customer_age} {years}! Де твої батьки?")
            elif int_customer_age < 16:
                print(f"Тобі лише {int_customer_age} {years}, а це фільм для дорослих!")
            elif int_customer_age > 65:
                print(f"Вам {int_customer_age} {years}? Покажіть пенсійне посвідчення!")
            else:
                print(f"Незважаючи на те, що вам {int_customer_age} {years}, білетів всеодно нема!")
