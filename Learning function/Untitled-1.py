def car_horn():
 print("Beep Beep! Move away")
while True:
 en=input("Enter word :")
 if en== "horn":
  car_horn()
 elif en=="exit":
  print("Go out")
  break 
 else:
  print("Unknow command! Try agin.")
