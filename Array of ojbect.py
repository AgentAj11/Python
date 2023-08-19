class Student:
    """Array of objects"""
    def __init__(self, name, age, gender, passion):
        self.name = name
        self.age = age
        self.gender = gender
        self.passion = passion

    def info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Passion : {self.passion}")


def main():
    students = []
    students.append(Student("Ajay Gaurav", 21.5, "M", "Farming"))
    students.extend([Student("Geeta", 29, "F", "Yoga"), Student("Sita", 24, "F", "Teaching"), Student("Radhe", 21, "M", "Engineering")])

    print(f"Number of students = {len(students)}\n")
    print("Students\n")
    for student in students:
        student.info()
        print("")

main()
