code="Start2026"
current_mode="Eco"
timeing=0
while True:
    e=input("Enter the turn code :").strip()
    if e != "Start2026" :
        print ("Access Denid!")
        timeing=timeing+1
        if timeing==3:
            print("ALARM! Calling the police")
            break
    else :
        print("Ening Started! Welcome back")
        while True:
         ee=input("Enter the current mode :")

         if ee == current_mode :
            print("You are already on Eco mode")
         else:
            print("Mode changed successfully to " + (ee))
            break
    break   
