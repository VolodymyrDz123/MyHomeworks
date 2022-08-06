from enum import Enum


class DiscountPoints(Enum):
    PRICE_OVER50 = (0.5, 50)
    PRICE_OVER100 = (1.5, 100)
    PRICE_OVER250 = (2.0, 250)
    PRICE_OVER300 = (3.0, 300)

    def __init__(self, discount, price):
        self.discount = discount
        self.price = price


def spices(cls):
    def wrapper():
        def add_sugar(self):
            self.price += 50
        cls.add_sugar = add_sugar

        def add_syrop(self):
            self.price += 150
        cls.add_syrop = add_syrop

        def add_cinnamon(self):
            self.price += 250
        cls.add_cinnamon = add_cinnamon
        return cls
    return wrapper()


@spices
class Latte:
    def __init__(self):
        self.price = 55
        self.name = Latte


@spices
class Cappuccino:
    def __init__(self):
        self.price = 60
        self.name = Cappuccino


@spices
class Espresso:
    def __init__(self):
        self.price = 40
        self.name = Espresso


class CoffeeMachine:
    def __init__(self):
        self.money = 0

    @staticmethod
    def get_discount(coffee_price):
        if coffee_price >= tuple(DiscountPoints.__members__.values())[3].price:
            return tuple(DiscountPoints.__members__.values())[3].discount
        if coffee_price >= tuple(DiscountPoints.__members__.values())[2].price:
            return tuple(DiscountPoints.__members__.values())[2].discount
        if coffee_price >= tuple(DiscountPoints.__members__.values())[1].price:
            return tuple(DiscountPoints.__members__.values())[1].discount
        if coffee_price >= tuple(DiscountPoints.__members__.values())[0].price:
            return tuple(DiscountPoints.__members__.values())[0].discount
        return 0

    def calculation(self, expected_coffee, human):
        if expected_coffee.price <= self.money:
            discount = expected_coffee.price * CoffeeMachine.get_discount(expected_coffee.price)/100
            change = self.money - (expected_coffee.price - discount)
            self.money = 0
            human.money += change
            return f"Ваш напій готовий, знято {expected_coffee.price - discount},знижка {discount} грн, здача {round(change, 2)} грн повернута"
        return f"У автоматі недостатньо коштів, зараз наявно - {self.money}, а необхідно - {expected_coffee.price}"


class Human:
    def __init__(self, name: str, surname: str, money: int):
        self.name = name
        self.surname = surname
        self.money = money

    def give_money(self, money: int, coffee_machine: CoffeeMachine):
        if self.money < money:
            return f"У вас {self.money}, ви не можете вставити у апарат {money}"
        coffee_machine.money += money
        self.money -= money
        return f"{self.money} вставлено у апарат"

    def order(self, coffee_machine: CoffeeMachine):
        expected_coffee = input("Виберіть яку каву ви хочете(\"latte\", \"cappuccino\" та \"espresso\"): ")
        if expected_coffee != "latte" and expected_coffee != "cappuccino" and expected_coffee != "espresso":
            return "Ви ввели не вірну назву кави, в наявності лише \"latte\", \"cappuccino\" та \"espresso\""
        else:
            if expected_coffee == "latte":
                expected_coffee = Latte()
            elif expected_coffee == "cappuccino":
                expected_coffee = Cappuccino()
            elif expected_coffee == "espresso":
                expected_coffee = Espresso()
            expected_spices = input("Якщо бажаєте додати \"sugar\" \"syrop\" або \"cinnamon\" то введіть назву добавки, а якщо ні - залишіть поле пустим: ")
            if expected_spices == "sugar":
                expected_coffee.add_sugar()
            elif expected_spices == "syrop":
                expected_coffee.add_syrop()
            elif expected_spices == "cinnamon":
                expected_coffee.add_cinnamon()
            return coffee_machine.calculation(expected_coffee, self)


if __name__ == "__main__":
    human_1 = Human("Vova", "Dz", 500)
    coffee_machine_1 = CoffeeMachine()
    print(human_1.__dict__)
    print(human_1.give_money(400, coffee_machine_1))
    print(human_1.order(coffee_machine_1))
    print(human_1.__dict__)
