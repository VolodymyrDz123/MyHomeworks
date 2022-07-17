import decimal
"""
Створити клас Vehicle (транспортний засіб):
ні від чого не наслідується
в ініціалізатор класу (__init__ метод) передати
producer: str
model: str
year: int
tank_capacity: float # обєм паливного баку
tank_level: float = 0 # початковий параметр рівня паливного баку дорівнює 0, параметр в аргументах не передавати
maxspeed: int
fuel_consumption: float # litres/100km споживання пального
odometer_value: int = 0 # при сході з конвеєра пробіг нульовий, параметр в аргументах не передавати
визначити метод __repr__, яким повертати інформаційну стрічку (наповнення на ваш вибір, проте параметри model and year
and odometer_value мають бути передані
написати метод refueling, який не приймає жодного аргумента, заправляє автомобіль на уявній автозаправці до максимума
(tank_level = tank_capacity), після чого виводить на екран повідомлення, скільки літрів було заправлено (перша заправка
буде повного баку, а в інших випадках величина буде залежати від залишку пального в баку)
написати метод race, який приймає один аргумент (не враховуючи self) - відстань, яку потрібно проїхати, а повертає
словник, в якому вказано, скільки авто проїхало, з огляду на заповнення паливного баку перед поїздкою, залишок пального
(при малому кілометражі все пальне не використається), та час, за який відбулася дана поїздка, з урахування, що середня
швидкість складає 80% від максимальної (витрата пального рівномірна незалежно від швидкості)
за результатами роботи метода в атрибуті tank_level екземпляра класа має зберігатися залишок пального після поїздки
(зрозуміло, що не менше 0)
збільшити на величину поїздки показники odometer_value
написати метод lend_fuel, який приймає окрім self ще й other обєкт, в результаті роботи якого паливний бак обєкта, на
якому було викликано відповідний метод, наповнюється до максимального рівня за рахунок відповідного зменшення рівня
пального у баку дружнього транспортного засобу
вивести на екран повідомлення з текстом типу "Дякую, бро, виручив. Ти залив мені *** літрів пального"
у випадку, якщо бак першого обєкта повний або у другого обєкта немає пального, вивести повідомлення "Нічого страшного,
якось розберуся"
написати метод get_tank_level, для отримання інформації про залишок пального конкретного інсттанса
написати метод get_mileage, який поверне значення пробігу odometer_value
написати метод __eq__, який приймає окрім self ще й other обєкт (реалізація магічного методу для оператора
порівняння == )
даний метод має повернути True у випадку, якщо 2 обєкта, які порівнюються, однакові за показниками року випуску та
пробігу (значення відповідних атрибутів однакові, моделі можуть бути різними)
створіть не менше 2-х обєктів класу, порівняйте їх до інших операцій, заправте їх, покатайтесь на них на різну відстань,
перевірте пробіг, позичте один в одного пальне, знову порівняйте
"""


def liters_ending(entry_liters):
    """
    Function for determine the correct ending for the word "літр"
    :param entry_liters: liters
    :type: int
    :return: the word "літр" with correct ending
    """
    str_entry_liters = str(entry_liters)
    if len(str_entry_liters) > 1 and str_entry_liters[-2] == "1":
        return "літрів"
    elif str_entry_liters.endswith("1"):
        return "літр"
    elif str_entry_liters.endswith("2") or str_entry_liters.endswith("3") or str_entry_liters.endswith("4"):
        return "літри"
    else:
        return "літрів"


class Vehicle:
    def __init__(self, producer: str, model: str, year: int, tank_capacity: float, maxspeed: int, fuel_consumption: float, odometer_value: int = 0, tank_level: float = 0):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.tank_level = tank_level
        self.maxspeed = maxspeed
        self.fuel_consumption = fuel_consumption
        self.odometer_value = odometer_value

    def __repr__(self):
        return f"Producer: {self.producer}, Model: {self.model}, Year: {self.year}, Odometer value: {self.odometer_value}"

    def refueling(self):
        if self.tank_level == self.tank_capacity:
            print(f"У тебе повний бак! {self.tank_level} {liters_ending(self.tank_level)}")
        else:
            filled = self.tank_capacity - self.tank_level
            self.tank_level += filled
            print(f"Було заправлено {filled} {liters_ending(self.tank_level)}")

    def race(self, expected_distance):
        actual_distance = 0
        while actual_distance < expected_distance:
            if self.tank_level > 0.1:
                self.odometer_value += 1
                self.tank_level -= 1 * (self.fuel_consumption / 100)
                actual_distance += 1
            else:
                break
        speed = self.maxspeed * 0.8
        time = actual_distance / speed

        return {"Авто проїхало": actual_distance, "Залишок пального": self.tank_level, "Час, за який відбулася дана поїздка": time}

    def lend_fuel(self, other):
        if self.tank_level == self.tank_capacity or other.tank_level == 0:
            print("Нічого страшного, якось розберуся")
        else:
            need_fill = 0
            while self.tank_level < self.tank_capacity:
                if other.tank_level > 0:
                    other.tank_level -= 0.1
                    self.tank_level += 0.1
                    need_fill += 0.1
                else:
                    break
            print(f"Дякую, бро, виручив. Ти залив мені {need_fill} {liters_ending(self.tank_level)} пального")

    def get_tank_level(self):
        return self.tank_level

    def get_mileage(self):
        return self.odometer_value

    def __eq__(self, other):
        return self.year == other.year and self.odometer_value == other.odometer_value


car_1 = Vehicle("Ford", "Fusion", 2016, 65, 150, 10)
car_2 = Vehicle("Audi", "Q5", 2015, 40, 150, 10)
print(car_2.__dict__)
car_1.__eq__(car_2)
car_1.refueling()
car_2.refueling()
print(car_1.race(20))
print(car_1.race(30))
print(car_2.race(2000))
print(car_1.get_mileage())
print(car_2.get_mileage())
car_2.lend_fuel(car_1)
print(car_2.__dict__)
car_1.__eq__(car_2)
