class CAR:
    def __init__(self,brand,base_price):
        self.brand=brand
        self.base_price=base_price
    def get_price(self):
        return self.base_price
class ElectricCar(CAR):
    def add_charger(self,charger_cost):
        self.charger_cost=charger_cost
    def get_total_price(self):
        total_price=self.base_price + self.charger_cost
        return total_price
brand=input("Enter your brand : ")
price=int(input("Enter the price : "))
charger_cost=int(input("Enter the charger cost : "))
my_car=ElectricCar(brand,price)
my_car.add_charger(charger_cost)
final_price=my_car.get_total_price()
print("THE CAR IS " + my_car.brand , " | THE PRICE IS " +str(my_car.base_price) , " THE TOTAL PRICE IS " + str(final_price))
