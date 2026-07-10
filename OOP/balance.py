class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,new_amount):
        if new_amount > 0 :
            self.__balance = new_amount
        else :
            print("You can not put the balance")
account= BankAccount("Eman" , 2000)
print(account.get_balance())
print(account.set_balance(-50))
