class BankAccount:
    def __init__(self,name_customer,financial_transaction):
        self.name_customer=name_customer
        self.financial_transaction=financial_transaction
    def get_fees(self):
        get_fees=5
        return get_fees
class InvestmentAccount(BankAccount):
    def get_fees(self):
        total_fees=self.financial_transaction * 0.02
        return total_fees
name_customer=input("Enter the customer name :")
financial_transaction=float(input("Enter value of the financial transaction :"))
my_account=InvestmentAccount(name_customer,financial_transaction)
my_fees=my_account.get_fees()
print("The customer name is : "+name_customer," | the discount fees is : "+str(my_fees))
