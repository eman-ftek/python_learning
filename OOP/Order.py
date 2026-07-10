class Order():
    def __init__(self,item_name,price):
        self.item_name=item_name
        self.price=price
    def calculate_total(self):
        return price
class ExpressOrder(Order):
    def add_shipping(self,shipping_cost):
        self.shipping_cost=shipping_cost
    def calculate_express_total(self):
        calculate_express_total =self.price + self.shipping_cost
        return calculate_express_total
name=input("Enter the item name : ")
price=int(input("Enter the price of the item : "))
shipping=int(input("Enter the cost of the shipping the item : "))
my_item=ExpressOrder(name,price)
my_item.add_shipping(shipping)
final_calculate=my_item.calculate_express_total()
print("The item name is : " + my_item.item_name )
print("The total price is : " + str(my_item.price)) 
print("The calculate total is : " + str(final_calculate))
