from copy import deepcopy
import pyfiglet
"""
Task 2. Вести з консолі строку зі слів (або скористайтеся константою). 
Напишіть код, який визначить кількість кількість слів, в цих даних.
"""

every_word_number = 0
my_string = input("Введіть кілька слів: ")
if not my_string.strip(" "):
    print("Тут не має бути пусто")
else:
    for every_word in my_string.split():
        every_word_number += 1
    print(f"Кількість слів у \"{my_string}\" = {every_word_number}")

"""
Task 3. Існує ліст з різними даними, наприклад 
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть механізм, який сформує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1. 
Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
"""

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = deepcopy(lst1)
for in_list1 in lst1:
    if type(in_list1) != int and type(in_list1) != float:
        lst2.remove(in_list1)
list2_print = pyfiglet.figlet_format(f"Values with type \"int\" ot \"float\" for \"lst1\" are \n {lst2}", font="bubble")
print(list2_print)
