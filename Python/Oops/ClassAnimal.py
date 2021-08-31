class Animal:

    @staticmethod
    def eat():
        print("Animal can eat!")


class Dog(Animal):
    @staticmethod
    def bark():
        print("Dog can bark!")


class Cat(Animal):

    @staticmethod
    def meown(self):
        print("Cat can meown")


animal_obj = Animal()
dog_obj = Dog()

dog_obj.eat()
dog_obj.bark()
