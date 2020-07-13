class Student:
    school = 'Cambridge'

    def __init__(self, m1, m2, m3):
        self.m1 = input("Enter the M1 mark:")
        self.m2 = input("Enter the M1 mark:")
        self.m3 = input("Enter the M1 mark:")

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def info(cls):
        return cls.school


s1 = Student()
# s2=Student()

print(s1.avg())
