import datetime
import myschool
import pytest


@pytest.fixture
def school_creating():
    return myschool.School("N1")


def test_creating_director(school_creating):
    director_1 = myschool.Director("director_1", "director_lastname", datetime.date(2000, 2, 20), school_creating)
    assert director_1.name == "director_1" and director_1.surname == "director_lastname" and \
           director_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_creating_headteacher(school_creating):
    headteacher_1 = myschool.HeadTeacher("headteacher_1", "headteacher_lastname", datetime.date(2000, 2, 20),
                                         school_creating)
    assert headteacher_1.name == "headteacher_1" and headteacher_1.surname == "headteacher_lastname" and \
           headteacher_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_creating_teacher(school_creating):
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    assert teacher_1.name == "teacher_1" and teacher_1.surname == "teacher_lastname" and \
           teacher_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_creating_learner(school_creating):
    learner_1 = myschool.Learner("learner_1", "learner_lastname", datetime.date(2000, 2, 20), school_creating)
    assert learner_1.name == "learner_1" and learner_1.surname == "learner_lastname" and \
           learner_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_creating_cleaner(school_creating):
    cleaner_1 = myschool.SchoolCleaner("cleaner_1", "cleaner_lastname", datetime.date(2000, 2, 20), school_creating)
    assert cleaner_1.name == "cleaner_1" and cleaner_1.surname == "cleaner_lastname" and \
           cleaner_1.age == (datetime.date.today() - datetime.date(2000, 2, 20)).days // 365


def test_schoolclass_learners(school_creating):
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    assert len(school_class_1.learners) == 0


def test_add_learners(school_creating):
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    learner_2 = myschool.Learner("learner_2", "learner_lastname2", datetime.date(2000, 2, 20), school_creating)
    learner_3 = myschool.Learner("learner_3", "learner_lastname3", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    school_class_1.add_learner(learner_2)
    school_class_1.add_learner(learner_3)
    assert len(school_class_1.learners) == 3


def test_delete_learners(school_creating):
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    learner_2 = myschool.Learner("learner_2", "learner_lastname2", datetime.date(2000, 2, 20), school_creating)
    learner_3 = myschool.Learner("learner_3", "learner_lastname3", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    school_class_1.add_learner(learner_2)
    school_class_1.add_learner(learner_3)
    school_class_1.delete_learner(learner_2)
    school_class_1.delete_learner(learner_3)
    assert len(school_class_1.learners) == 1


def test_correct_school_fees(school_creating):
    director_1 = myschool.Director("director_1", "director_lastname", datetime.date(2000, 2, 20), school_creating)
    headteacher_1 = myschool.HeadTeacher("headteacher_1", "headteacher_lastname", datetime.date(2000, 2, 20),
                                         school_creating)
    cleaner_1 = myschool.SchoolCleaner("cleaner_1", "cleaner_lastname", datetime.date(2000, 2, 20), school_creating)
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    learner_2 = myschool.Learner("learner_2", "learner_lastname2", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_2)
    assert school_creating.get_school_fees(1000) == 'Кожен учень має заплатити по 22500.0 за рік'


def test_increase_school_fees(school_creating):
    director_1 = myschool.Director("director_1", "director_lastname", datetime.date(2000, 2, 20), school_creating)
    headteacher_1 = myschool.HeadTeacher("headteacher_1", "headteacher_lastname", datetime.date(2000, 2, 20),
                                         school_creating)
    cleaner_1 = myschool.SchoolCleaner("cleaner_1", "cleaner_lastname", datetime.date(2000, 2, 20), school_creating)
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    learner_2 = myschool.Learner("learner_2", "learner_lastname2", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_2)
    assert school_creating.get_school_fees(1000) == 'Кожен учень має заплатити по 22500.0 за рік'
    learner_3 = myschool.Learner("learner_3", "learner_lastname3", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_3)
    assert school_creating.get_school_fees(1000) == 'Кожен учень має заплатити по 15000.0 за рік'


def test_decrease_school_fees(school_creating):
    director_1 = myschool.Director("director_1", "director_lastname", datetime.date(2000, 2, 20), school_creating)
    headteacher_1 = myschool.HeadTeacher("headteacher_1", "headteacher_lastname", datetime.date(2000, 2, 20),
                                         school_creating)
    cleaner_1 = myschool.SchoolCleaner("cleaner_1", "cleaner_lastname", datetime.date(2000, 2, 20), school_creating)
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    learner_2 = myschool.Learner("learner_2", "learner_lastname2", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_2)
    assert school_creating.get_school_fees(1000) == 'Кожен учень має заплатити по 22500.0 за рік'
    school_class_1.delete_learner(learner_2)
    school_creating.learners.remove(learner_2)
    assert school_creating.get_school_fees(1000) == 'Кожен учень має заплатити по 45000.0 за рік'


def test_learner_already_in_class(school_creating):
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    assert school_class_1.add_learner(learner_1) == "learner_1 already in the class"


def test_learner_average_mark(school_creating):
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    teacher_1.mark(12, learner_1)
    teacher_1.mark(12, learner_1)
    teacher_1.mark(8, learner_1)
    assert learner_1.get_average_mark() == 'Середня оцінка для learner_1 learner_lastname1 становить "10.7"'


def test_class_marks(school_creating):
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    learner_2 = myschool.Learner("learner_2", "learner_lastname2", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_2)
    teacher_1.mark(12, learner_1)
    teacher_1.mark(9, learner_1)
    teacher_1.mark(5, learner_2)
    assert school_class_1.get_class_marks() == 'Середня оцінка класу становить "8.7" балів'


def test_school_marks(school_creating):
    teacher_1 = myschool.Teacher("teacher_1", "teacher_lastname", datetime.date(2000, 2, 20), school_creating)
    school_class_1 = myschool.SchoolClass(school_creating, "1-A", teacher_1)
    school_class_2 = myschool.SchoolClass(school_creating, "1-B", teacher_1)
    learner_1 = myschool.Learner("learner_1", "learner_lastname1", datetime.date(2000, 2, 20), school_creating)
    school_class_1.add_learner(learner_1)
    learner_2 = myschool.Learner("learner_2", "learner_lastname2", datetime.date(2000, 2, 20), school_creating)
    school_class_2.add_learner(learner_2)
    teacher_1.mark(5, learner_1)
    teacher_1.mark(6, learner_1)
    teacher_1.mark(7, learner_1)
    assert school_creating.get_school_marks() == 'Середня оцінка школи становить "6.0" балів'


