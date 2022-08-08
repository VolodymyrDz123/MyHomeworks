"""
До вже зробленого завдання по приватній школі описати Учня, Вчителя, Персонал, Людину, Завуча та Директора як Data Classes.
Також до всіх осіб додати поле стать, яку слід виразити як Enum.
"""
import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Sex(Enum):
    MAN = "man"
    WOMAN = "woman"


class School:
    def __init__(self, name: str):
        self.name = name
        self.SchoolClass = []
        self.teachers = []
        self.learners = []
        self.cleaners = []
        self.director = None
        self.head_teacher = None

    def get_school_fees(self):
        try:
            expected_profit = int(input("Вкажіть який школа має отримати прибуток за рік: "))
        except ValueError:
            return "Прибуток має бути в цифрах, наприклад \"10000\""
        all_salary = 0
        for teacher in self.teachers:
            all_salary += teacher.salary
        for cleaner in self.cleaners:
            all_salary += cleaner.salary
        all_salary += self.director.salary
        all_salary += self.head_teacher.salary
        try:
            in_come = (all_salary + expected_profit) / len(self.learners)
        except ZeroDivisionError:
            return f"У школі поки що немає учнів"
        return f"Кожен учень має заплатити по {round(in_come, 1)} за рік"

    def get_school_marks(self):
        total = 0
        learners = 0
        for learner in self.learners:
            for mark in learner.marks:
                total += mark
                learners += 1
        try:
            avg_mark = round(total / learners, 1)
        except ZeroDivisionError:
            return f"У жодного учня школи поки що немає балів"
        return f"Середня оцінка школи становить \"{avg_mark}\" балів"


@dataclass()
class Personal(ABC):
    name: str
    surname: str
    __age: datetime.date
    school: School
    sex: Sex

    @property
    def age(self):
        return (datetime.date.today() - self.__age).days // 365

    @abstractmethod
    def get_reward(self):
        pass


@dataclass()
class Learner(Personal):
    def __post_init__(self):
        self.position = "Learner"
        self.marks = []
        self.school.learners.append(self)

    def get_average_mark(self):
        if self.marks:
            average = 0
            for mark in self.marks:
                average += mark
            average_mark = round(average / len(self.marks), 1)
            return f"Середня оцінка для {self.name} {self.surname} становить \"{average_mark}\""
        else:
            return f"У {self.name} {self.surname} поки що відсутні оцінки"

    def get_reward(self):
        self.marks.append(12)
        return f"{self.name} отримав винагороду у вигляді оцінки \"12\"!"


@dataclass()
class Teacher(Personal):
    def __post_init__(self):
        self.position = "Teacher"
        self.salary = 6000
        self.school.teachers.append(self)
        self.school_class = None

    def get_school_class(self):
        if self.school_class:
            return f"Вчитель {self.name} призначений до класу {self.school_class}"
        else:
            return f"Вчитель {self.name} поки що не призначений до певного класу школи"

    def mark(self, mark_value: int, learner: Learner):
        if 1 <= mark_value <= 12:
            learner.marks.append(mark_value)
            return f"Вчитель {self.name} поставив оцінку \"{mark_value}\" для {learner.name}"
        else:
            return "Оцінка має бути від 1 до 12"

    def get_reward(self):
        return f"{self.name} отримав винагороду у вигляді зарплати \"{self.salary}\"!"


@dataclass()
class Director(Personal):
    def __post_init__(self):
        self.position = "Director"
        self.salary = 20000
        self.school.director = self

    def get_reward(self):
        return f"{self.name} отримав винагороду у вигляді зарплати \"{self.salary}\"!"


@dataclass()
class HeadTeacher(Personal):
    def __post_init__(self):
        self.position = "HeadTeacher"
        self.salary = 15000
        self.school.head_teacher = self

    def get_reward(self):
        return f"{self.name} отримав винагороду у вигляді зарплати \"{self.salary}\"!"


@dataclass()
class SchoolCleaner(Personal):
    def __post_init__(self):
        self.position = "Cleaner"
        self.salary = 3000
        self.school.cleaners.append(self)

    def get_reward(self):
        return f"{self.name} отримав винагороду у вигляді зарплати \"{self.salary}\"!"

    def clean(self):
        return f"Прибиральник {self.name} поприбирав у школі {self.school}"


class SchoolClass:
    def __init__(self, school: School, name, teacher: Teacher):
        self.school = school
        self.name = name
        self.learners = []
        self.teacher = teacher
        teacher.school_class = self.name
        school.SchoolClass.append(self.name)

    def add_learner(self, learner: Learner):
        self.learners.append(learner)

    def delete_learner(self, learner: Learner):
        self.learners.remove(learner)

    def get_learners(self):
        all_learners = []
        for learner in self.learners:
            all_learners.append(f"{learner.name} {learner.surname}")
        print(f"Учні класу {self.name}: {all_learners}")

    def change_teacher(self, new_teacher: Teacher):
        self.teacher.school_class = None
        self.teacher = new_teacher
        self.teacher.school_class = self.name
        return f"Новий класний керівник класу {self.name} {self.teacher.name}"

    def get_class_marks(self):
        total = 0
        learners = 0
        for learner in self.learners:
            for mark in learner.marks:
                total += mark
                learners += 1
        try:
            avg_mark = round(total / learners, 1)
        except ZeroDivisionError:
            return f"У жодного учня класу поки що немає балів"
        return f"Середня оцінка класу становить \"{avg_mark}\" балів"

    def delete_class(self):
        for every_lerner in self.learners:
            self.school.learners.remove(every_lerner)
        self.learners = []
        self.teacher.school_class = None
        self.school.SchoolClass.remove(self.name)
        return f" Клас {self.name} школи {self.school.name} розпущено, усі учні виключені"


if __name__ == "__main__":
    school_1 = School("N1")
    director_1 = Director("director_1", "lastname", datetime.date(2000, 2, 20), school_1, Sex.WOMAN.value)
    headteacher_1 = HeadTeacher("headteacher_1", "lastname", datetime.date(2000, 2, 20), school_1, Sex.MAN.value)
    teacher_1 = Teacher("teacher_1", "lastname", datetime.date(2000, 2, 20), school_1, Sex.MAN.value)
    teacher_2 = Teacher("teacher_2", "lastname", datetime.date(2000, 2, 20), school_1, Sex.WOMAN.value)
    school_class_1 = SchoolClass(school_1, "1-A", teacher_1)
    school_class_2 = SchoolClass(school_1, "1-Б", teacher_2)
    lerner_1 = Learner("lerner_1", "lastname", datetime.date(2000, 2, 20), school_1, Sex.MAN.value)
    lerner_2 = Learner("lerner_2", "lastname", datetime.date(2000, 2, 20), school_1, Sex.WOMAN.value)
    lerner_3 = Learner("lerner_3", "lastname", datetime.date(2000, 2, 20), school_1, Sex.MAN.value)
    cleaner_1 = SchoolCleaner("cleaner_1", "lastname", datetime.date(2000, 2, 20), school_1, Sex.WOMAN.value)

    school_class_1.add_learner(lerner_1)
    school_class_1.add_learner(lerner_2)
    school_class_2.add_learner(lerner_3)
    print(teacher_1.mark(12, lerner_1))
    print(teacher_1.mark(12, lerner_1))
    print(teacher_1.mark(8, lerner_2))
    print(teacher_2.mark(6, lerner_3))
    print(teacher_2.mark(2, lerner_3))
    print(lerner_1.get_average_mark())
    print(lerner_2.get_average_mark())
    print(lerner_3.get_average_mark())
    print(school_class_1.get_class_marks())
    print(school_1.get_school_marks())
    print(school_1.get_school_fees())
    print(teacher_1.__dict__)
    print(lerner_1.__dict__)
    print(director_1.__dict__)
    print(cleaner_1.__dict__)
    print(headteacher_1.__dict__)
