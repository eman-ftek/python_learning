class Customer:
    def __init__(self,name,total_amount):
        self.name=name
        self.total_amount=total_amount
    def calculate_discount(self):
        calculate_discount=0
        return calculate_discount
class VIBCustomer(Customer):
    def calculate_discount(self):
        calculate_discount=self.total_amount * 0.10
        return calculate_discount
name=input("Enter the VIB customer name : ")
total_amount=float(input("Enter the total amount for his boutgh : "))
my_item=VIBCustomer(name,total_amount)
discount_value=my_item.calculate_discount()
print("The customer name is : " + name , "| the discount value is : " + str(discount_value))
