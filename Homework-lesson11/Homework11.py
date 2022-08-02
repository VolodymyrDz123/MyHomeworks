"""
Технічне завдання.
Розробити програму, яка підрахує на основі зарплат вчителів, директора, заучів та прибиральників, скільки дітей та з
якою оплатою за навчання треба формувати класи на наступний навчальний рік.
Рівно так само програма має виводити середню оцінку учнів по класу і загалом по школі (для спрощення завдання учневі
ми приписуємо лише середній бал).
Деталі
Кожна людина має:
Імʼя
Прізвище
вік
посада згідно штатного розпису
Персонал школи є людьми, які мають:
Зарплату
В школі є наступний персонал:
Директор (зп - 20000 грн в місяць)
Завуч (зп - 15000 грн в місяць)
Вчитель (зп - 6000 грн в місяць)
Учень теж належить до персоналу, але: він платить за навчання... І якщо персонал отримує винагороду через отримання
зарплати, то учні отримують винагороду через гарні оцінки! (врахуйте це. Отимання винагороди - абстрактна дія, яка для
певних видів персоналу означає різне).
Школа містить у собі класів. Кожен клас має список учнів. Учнів можна до класу додавати, видаляти, виводити список учнів
на консоль. Також клас має учителя - класного керівника, що веде клас.
Класи можна додавати (додається пустий клас, але з класним керівником), видаляти (інші учні мають бути або переведеним
в інший клас, або виключеним зі школи).
"""
import datetime
from abc import ABC, abstractmethod


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
        except:
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



class Personal(ABC):
    def __init__(self, name: str, surname: str, age: datetime.date, school: School):
        self.name = name
        self.surname = surname
        self.__age = age
        self.name = name
        self.school = school.name

    @property
    def age(self):
        return (datetime.date.today() - self.__age).days // 365

    @abstractmethod
    def get_reward(self):
        pass


class Learner(Personal):
    def __init__(self, name: str, surname: str, age: datetime.date, school: School):
        super().__init__(
            name,
            surname,
            age,
            school,
        )
        self.position = "Learner"
        self.marks = []
        school.learners.append(self)

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

    def pay_fees(self):
        ...


class Teacher(Personal):
    def __init__(self, name: str, surname: str, age: datetime.date, school: School):
        super().__init__(
            name,
            surname,
            age,
            school,
        )
        self.position = "Teacher"
        self.salary = 6000
        school.teachers.append(self)
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


class Director(Personal):
    def __init__(self, name: str, surname: str, age: datetime.date, school: School):
        super().__init__(
            name,
            surname,
            age,
            school
        )
        self.position = "Director"
        self.salary = 20000
        school.director = self

    def get_reward(self):
        return f"{self.name} отримав винагороду у вигляді зарплати \"{self.salary}\"!"


class HeadTeacher(Personal):
    def __init__(self, name: str, surname: str, age: datetime.date, school: School):
        super().__init__(
            name,
            surname,
            age,
            school,
        )
        self.position = "HeadTeacher"
        self.salary = 15000
        school.head_teacher = self

    def get_reward(self):
        return f"{self.name} отримав винагороду у вигляді зарплати \"{self.salary}\"!"


class SchoolCleaner(Personal):
    def __init__(self, name: str, surname: str, age: datetime.date, school: School):
        super().__init__(
            name,
            surname,
            age,
            school,
        )
        self.position = "Cleaner"
        self.salary = 3000
        school.cleaners.append(self)

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
    director_1 = Director("director_1", "lastname", datetime.date(2000, 2, 20), school_1)
    headteacher_1 = HeadTeacher("headteacher_1", "lastname", datetime.date(2000, 2, 20), school_1)
    teacher_1 = Teacher("teacher_1", "lastname", datetime.date(2000, 2, 20), school_1)
    teacher_2 = Teacher("teacher_2", "lastname", datetime.date(2000, 2, 20), school_1)
    school_class_1 = SchoolClass(school_1, "1-A", teacher_1)
    school_class_2 = SchoolClass(school_1, "1-Б", teacher_2)
    lerner_1 = Learner("lerner_1", "lastname", datetime.date(2000, 2, 20), school_1)
    lerner_2 = Learner("lerner_2", "lastname", datetime.date(2000, 2, 20), school_1)
    lerner_3 = Learner("lerner_3", "lastname", datetime.date(2000, 2, 20), school_1)
    cleaner_1 = SchoolCleaner("cleaner_1", "lastname", datetime.date(2000, 2, 20), school_1)

    # print(school_1.get_school_fees())
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

