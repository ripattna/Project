class Animal:

    @staticmethod
    def eat():
        print("Animal can eat!")


class Dog(Animal):
    @staticmethod
    def bark():
        print("Dog can bark!")


class BabyDog(Dog):
    @staticmethod
    def weep():
        print("Baby_Dog can weep!")


BabyDog.weep()
BabyDog.eat()

# babyDog_obj = BabyDog

# babyDog_obj.weep()
# babyDog_obj.bark()
# babyDog_obj.eat()
