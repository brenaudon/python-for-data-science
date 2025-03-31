from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

print("-----")

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as e:
    print(e)
