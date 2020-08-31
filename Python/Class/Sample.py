class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Configuration of CPU:" + self.cpu)
        print("Configuration of RAM:", self.ram)


comp1 = Computer('i5', '8GB')
comp2 = Computer('i7', '16GB')
print(type(comp1))
comp1.config()
# comp2.config()
Computer.config(comp2)


