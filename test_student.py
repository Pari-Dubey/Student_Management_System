from student import *


def test_add_student():
    students.clear()
    add_student(1, "Pari", 95)
    assert len(students) == 1


def test_search_student():
    students.clear()
    add_student(1, "Pari", 95)
    assert search_student(1)["name"] == "Pari"


def test_update_student():
    students.clear()
    add_student(1, "Pari", 95)
    update_student(1, "Anjali", 90)
    assert search_student(1)["name"] == "Anjali"


def test_delete_student():
    students.clear()
    add_student(1, "Pari", 95)
    delete_student(1)
    assert search_student(1) is None


def test_view_students():
    students.clear()
    add_student(1, "Pari", 95)
    assert len(view_students()) == 1