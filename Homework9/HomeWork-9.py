"""
Завдання №1
Розробити клас Людина. Людина має:
Ім'я
Прізвище
Вік (атрибут але ж змінний)
Стать
Люди можуть:
Їсти
Спати
Говорити
Ходити
Стояти
Лежати
Також ми хочемо контролювати популяцію людства. Змінювати популяцію можемо в __init__. Треба сказати, що доступ до
статичних полів класу з __init__ не можу іти через НазваКласу.статичий_атрибут, позаяк ми не може бачити імені класу.
Але натомість ми можемо сказати self.__class__.static_attribute.
"""
import datetime


class Human:
    population = 0

    def __init__(self, first_name, last_name, birth_date, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.__birth_date = birth_date
        self.sex = sex
        self.__class__.population += 1

    def eat(self):
        return f"{self.first_name} їсть"

    def sleep(self):
        return f"{self.first_name} спить"

    def talk(self):
        return f"{self.first_name} говорить"

    def stand(self):
        return f"{self.first_name} стоїть"

    def lie(self):
        return f"{self.first_name} лежить"

    @property
    def age(self):
        return (datetime.date.today() - self.__birth_date).days // 365


person_1 = Human("Vova", "Last", datetime.date(2000, 2, 20), "male")
print(person_1.eat())
print(person_1.sleep())
print(person_1.talk())
print(person_1.stand())
print(person_1.lie())
print(person_1.age)
print(person_1.population)
