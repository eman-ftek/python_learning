password=input("Enter the password :").strip()
if len(password)<8 :
    print ("Very small")
elif len(password)==8 and password==("12345678") :
    print("Very waek password")
else:
    print("accept")  