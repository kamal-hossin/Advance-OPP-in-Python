class Student:
    school = "ABC School"   # Static Attribute

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Static Method
    @staticmethod
    def greet():
        print("Welcome to the School")

    # Class Method
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def average(a, b, c):
        return (a + b + c) / 3

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"School: {Student.school}")


s1 = Student("Kamal", 85)
s1.display()
Student.change_school("XYZ School")
print()
s1.display()
Student.greet()
avg = Student.average(80, 90, 100)
print("Average Marks:", avg)