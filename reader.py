import json

def read_students(file):
    with open(file, "r") as file:
        students = json.load(file)
        return students

students = read_students("student_data.json")
for i in students:
    print(i)