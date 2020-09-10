from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


## Forest factory definition
class ForestFactory:
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == "__main__":
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat? ")
    ff.make_sound(animal)
