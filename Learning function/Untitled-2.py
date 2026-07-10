def walcom_driver(name):
    print("Welcom back, Captain " +name)
def check_speed(speed):
    if speed > 120 :
        print("DOWN!Too Fast!")
    else:
        print("Safe speed. Enjoy your drive")
name_user= input("Your name :")
walcom_driver(name_user)
while True :
    inpu=int(input("Enter the speed :"))
    if inpu ==0 :
        print("Car Stopped")
        break
    else:
        check_speed(inpu) 
                         