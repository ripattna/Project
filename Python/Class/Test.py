class Computer:
    # pass
    def __init__(self):
        self.name = input("Enter the name of the person:")
        self.age = int(input("Enter the age of the person: "))

    def update(self):
        self.age = 26

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
print(id(c1))

if c1.compare(c2):
    print("They are same:")
else:
    print("They are not equal")

print("The name of person is:", c1.name)
print("The age of person is:", c1.age)

print("The name of person is:", c2.name)
print("The age of person is:", c2.age)
