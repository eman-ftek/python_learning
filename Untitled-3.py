while True:
 p=input("Enter your password :").strip() 
 if len(p)<8:
    print("Very small") 
 elif len(p)==8 and p==("12345678"):
    print("Very waek")     
 else :
    print("Accept")
    break   
