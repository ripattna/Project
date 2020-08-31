class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("Name is: " + self.name)
        print("Color is: " + self.color)
        print("Weight is:" + str(self.weight))


r_obj1 = Robot("Nisan", "Brown", 70)
r_obj2 = Robot("Ris", "Brown", 50)

r_obj1.introduce_self()

r_obj2.introduce_self()


