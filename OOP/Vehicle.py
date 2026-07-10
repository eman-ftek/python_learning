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
name=input("Enter the model car : ")
my_statu=Ambulance(name)
speed=my_statu.get_max_speed()
print("The car model is : " + name , " | the max speed allow it is : " + str(speed))
