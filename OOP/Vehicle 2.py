def check_radar(obj):
    print("The speed is " +str(obj.get_max_speed()))
class Vehicle:
    def __init__(self,model):
        self.model=model
    def get_max_speed(self):
        max_speed=120
        return max_speed
class Ambulance(Vehicle):
    def get_max_speed(self):
        total_max_speed= super().get_max_speed()+ 40
        return total_max_speed
car=Vehicle("BMW")
amb=Ambulance("Toyota")
check_radar(car)
check_radar(amb)
