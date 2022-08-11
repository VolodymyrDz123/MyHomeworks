import datetime
import Homework16


def test_creating_director():
    school_1 = Homework16.School("N1")
    director_1 = Homework16.Director("director_1", "director_lastname", datetime.date(2000, 2, 20), school_1)
    assert director_1.name == "director_1" and director_1.surname == "director_lastname" and \
           director_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_creating_headteacher():
    school_1 = Homework16.School("N1")
    headteacher_1 = Homework16.HeadTeacher("headteacher_1", "headteacher_lastname", datetime.date(2000, 2, 20), school_1)
    assert headteacher_1.name == "headteacher_1" and headteacher_1.surname == "headteacher_lastname" and \
           headteacher_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_creating_teacher():
    school_1 = Homework16.School("N1")
    teacher_1 = Homework16.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_1)
    assert teacher_1.name == "teacher_1" and teacher_1.surname == "teacher_lastname" and \
           teacher_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_creating_learner():
    school_1 = Homework16.School("N1")
    lerner_1 = Homework16.Learner("lerner_1", "lerner_lastname", datetime.date(2000, 2, 20), school_1)
    assert lerner_1.name == "lerner_1" and lerner_1.surname == "lerner_lastname" and \
           lerner_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_creating_cleaner():
    school_1 = Homework16.School("N1")
    cleaner_1 = Homework16.SchoolCleaner("cleaner_1", "cleaner_lastname", datetime.date(2000, 2, 20), school_1)
    assert cleaner_1.name == "cleaner_1" and cleaner_1.surname == "cleaner_lastname" and \
           cleaner_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_schoolclass_learners():
    school_1 = Homework16.School("N1")
    teacher_1 = Homework16.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_1)
    school_class_1 = Homework16.SchoolClass(school_1, "1-A", teacher_1)
    assert len(school_class_1.learners) == 0


def test_add_learners():
    school_1 = Homework16.School("N1")
    teacher_1 = Homework16.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_1)
    school_class_1 = Homework16.SchoolClass(school_1, "1-A", teacher_1)
    lerner_1 = Homework16.Learner("lerner_1", "lerner_lastname1", datetime.date(2000, 2, 20), school_1)
    lerner_2 = Homework16.Learner("lerner_2", "lerner_lastname2", datetime.date(2000, 2, 20), school_1)
    lerner_3 = Homework16.Learner("lerner_3", "lerner_lastname3", datetime.date(2000, 2, 20), school_1)
    school_class_1.add_learner(lerner_1)
    school_class_1.add_learner(lerner_2)
    school_class_1.add_learner(lerner_3)
    assert len(school_class_1.learners) == 3


def test_delete_learners():
    school_1 = Homework16.School("N1")
    teacher_1 = Homework16.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_1)
    school_class_1 = Homework16.SchoolClass(school_1, "1-A", teacher_1)
    lerner_1 = Homework16.Learner("lerner_1", "lerner_lastname1", datetime.date(2000, 2, 20), school_1)
    lerner_2 = Homework16.Learner("lerner_2", "lerner_lastname2", datetime.date(2000, 2, 20), school_1)
    lerner_3 = Homework16.Learner("lerner_3", "lerner_lastname3", datetime.date(2000, 2, 20), school_1)
    school_class_1.add_learner(lerner_1)
    school_class_1.add_learner(lerner_2)
    school_class_1.add_learner(lerner_3)
    school_class_1.delete_learner(lerner_2)
    school_class_1.delete_learner(lerner_3)
    assert len(school_class_1.learners) == 1
