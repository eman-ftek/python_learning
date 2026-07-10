class Animal:
    def make_sound(self):
        return "Generic Animal Sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof Woof"
animal_1=Animal()
animal_2=Dog()
print(animal_1.make_sound())
print(animal_2.make_sound())
