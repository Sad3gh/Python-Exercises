from abc import ABC,abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(f"{animal.name} says {animal.speak()}")

my_cat = Cat("Ainaz")
my_dog = Dog("Anthony")
animal_sound(my_cat)
animal_sound(my_dog)
