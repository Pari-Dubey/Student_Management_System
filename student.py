students = []

# 1. Add Student:
def add_student(roll, name, marks):
    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    students.append(student)
    return "Student Added Successfully"


# 2. View Students:
def view_students():
    return students


# 3. Search Students
def search_student(roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def update_student(roll, new_name, new_marks):
    for student in students:
        if student["roll"] == roll:
            student["name"] = new_name
            student["marks"] = new_marks
            return "Student Updated Successfully"
    return "Student Not Found"


def delete_student(roll):
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            return "Student Deleted Successfully"
    return "Student Not Found"