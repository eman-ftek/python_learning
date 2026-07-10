class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def show_speed(self):
        print("The car name :" + self.brand, "| The speed :" + str(self.speed))
    def accelerate(self,amount):
        self.speed=self.speed + amount  
        print("Vroom! Tesla accelerated ")
my_car=Car("Tesla",150)
my_car.show_speed()
my_car.accelerate(40)
my_car.show_speed()          
