class BankAccount:
    def __init__(self,owner,balance):
     self.owner=owner
     self.balance=balance
    def show_info(self):
        print("Account Owner :"+ self.owner + "|Balance :" + str(self.balance))
my_account=BankAccount("Eman" ,5000)
my_account.show_info()
