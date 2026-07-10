balance=500
time=0
while True:
    PIN=input("Enter the PIN :").strip()
    if PIN != "1122" :
        print("Wrong PIN!")
        time=time+1
        if time==3:
         print("Your card has been swallowed!")
         break
    else :
        print("Correct PIN")
        m=int(input("Enter the monye "))
        if m>balance :
         print("Incompatible balance")
        else:
         balance=balance-m
         print("Successful operation"+str(balance))
         break

