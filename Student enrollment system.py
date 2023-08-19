class Course:
    def __init__(self, course_name, course_code, course_duration, course_seats, course_prerequisite):
        self.course_name = course_name
        self.course_code = course_code
        self.course_prerequisite = course_prerequisite
        self.course_duration = course_duration
        self.course_seats = course_seats
        self.students = []  # to store enrolled students

    def info(self):
        print(f"Course name : {self.course_name}")
        print(f"Course code : {self.course_code}")
        print(f"Course prerequisite : {self.course_prerequisite}")
        print(f"Course duration : {self.course_duration}")
        print(f"Course seats : {self.course_seats}")

    def student_enrolled(self):
        return len(self.students)

    def add_student(self, student):
        if len(self.students) < self.course_seats:
            self.students.append(student)
            return True
        return False


class Student:
    def __init__(self, name, age, gender, marks):
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Marks : {self.marks}")


def main():
    # course
    microprocessor = Course("Microprocessor", "PCS-501", "10 Weeks", 3, "Digital Logic")
    microprocessor.info()
    print(f"Student enrolled = {microprocessor.student_enrolled()}")

    # student
    students = [Student("Ajay Gaurav", 21.5, "M", 99), Student("Geeta", 29, "F", 90), Student("Sita", 24, "F", 77), Student("Radhe", 21, "M", 47)]

    # enroll the students
    print("")
    print("Enrollment process")
    for student in students:
        if microprocessor.add_student(student):
            print(f"{student.name} enrolled")
        else:
            print(f"{student.name} not enrolled")
    print("")
    print(f"Enrolled students = {microprocessor.student_enrolled()}")

    for student in microprocessor.students:
        student.info()
        print("")


main()
