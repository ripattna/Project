class Student:
    school = 'Cambridge'

    def __init__(self, m1, m2, m3):
        self.m1 = int(input("Enter the M1 mark:"))
        self.m2 = int(input("Enter the M1 mark:"))
        self.m3 = int(input("Enter the M1 mark:"))

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def info(cls):
        return cls.school


s1 = Student(m1, m2, m3)
# s2=Student()

print(s1.avg())

