from abc import ABC, abstractmethod
class DrinkMachin(ABC):
    @abstractmethod
    def make_drink(self):
        pass
class EspressoMachin(DrinkMachin):
    def make_drink(self):
        return("The espresso is preparation began")
class TeaMachin(DrinkMachin):
    def make_drink(self):
        return("The tea is preparation began")
my_order=EspressoMachin()
print(my_order.make_drink())
my_tea=TeaMachin()
print(my_tea.make_drink())
