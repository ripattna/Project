class Animal:

    @staticmethod
    def eat():
        print("Animal can eat!")


class Cat:

    @staticmethod
    def sleep():
        print("Cat can sleep!")


class Dog(Animal, Cat):

    @staticmethod
    def eat():
        print("Dog can bark!")


'''
d = Dog()
d.sleep()
d.eat()
'''

Dog.eat()
Dog.sleep()
