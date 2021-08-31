class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()

    def show(self):
        print("The name is:", self.name, "The Age is:", self.age)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8GB'

        def show(self):
            return print(self.brand, self.cpu, self.ram)


s1 = Student("Ram", 26)
s2 = Student("Harish", 28)

s1.show()
s2.show()

# s1.lap.brand

# lap1 = s1.lap
# lap2 = s2.lap

# lap1 = Student.Laptop()
