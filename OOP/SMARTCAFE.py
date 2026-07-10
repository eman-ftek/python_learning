class SMARTCAFE:
 def __init__(self,customer_name):
    self.customer_name=customer_name
    self.total_cost=0
 def add_item(self,price):
  self.total_cost=self.total_cost + price
  print("Item added")
 def show_bill(self):
    print("Our dear "+ self.customer_name +" the total_cost is "+ str(self.total_cost))
your_name=input("Your name :")
my_cafe=SMARTCAFE(your_name)
while True:
    chose=input("Enter your chose :")
    if chose=='1':
        price=float(input("Write price :"))
        my_cafe.add_item(price)
    elif chose=='2':
        my_cafe.show_bill()
    else:
        my_cafe.show_bill()
        break       
