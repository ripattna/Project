'''class Computer:

    def config(self):
        print("The Config of the PC is")

comp1 = Computer()
comp2 = Computer()
Computer.config(comp1)
Computer.config(comp2)

comp1.config()
comp2.config()
'''


class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu, self.ram)


comp1 = Computer('i5', '8GB')
comp2 = Computer('i7', '16GB')
print(type(comp1))
comp1.config()
comp2.config()
