from abc import ABC, abstractmethod 
class Character(ABC):
 @ abstractmethod
 def attack(self):
    pass
class Warrior(Character):
    def attack(self):
        return("The warrior attacks with a sharp sword")
my_hero=Warrior()
print(my_hero.attack())