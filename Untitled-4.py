t=0
while True:
 passwerd= input("Enter your passwerd :").strip()
 if len(passwerd)<8:
      print("Very samll")
      t=1+t
 elif len(passwerd)==8 and passwerd==("12345678"):
      print("Very waek")
      t=1+t
 else:
      print("Accept")
      break
 if t==3 :
    print("Account Loked")
    break