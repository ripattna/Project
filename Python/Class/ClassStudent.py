class Student:

    school = 'Cambridge'

    def __init__(self, m1, m2, m3):
        self.m1 = int(input("Enter the M1 mark:"))
        self.m2 = int(input("Enter the M1 mark:"))
        self.m3 = int(input("Enter the M1 mark:"))

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student Class..In Module XYZ")


s1 = Student(10, 20, 50)
# s2=Student()

print(s1.avg())
print("School is:", Student.getSchool())
Student.info()

