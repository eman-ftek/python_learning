import json
import hashlib
import datetime
class BankSystem:
    def __init__(self):
        self.db_name = "bank_db.json"
    def hash_pin(self,pin):
        hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
        return hashed_pin
    def load_account(self):
        try:
            file_read = open(self.db_name , "r")
            account = json.load(file_read)
            file_read.close()
            if isinstance(account,list):
                return account
            return [account]
        except Exception as e:
            print("Notice : " , e)
            return []
    def login(self,account_no,pin):
        account = self.load_account()
        hashed_pin = self.hash_pin(pin)
        for acc in account:
          if isinstance(acc,dict):  
            if acc["account_no"] == account_no and acc["pin"] == hashed_pin :
                print("Welome "+ acc["customer_name"] , "Your balanc is " + str(acc["balanc"]))
                return acc
                self.log_event("LOGIN_SUCCES", f"Acount No: {account_no}")
        print("Error: Account number or pin is incorrect!")
        self.log_event("LOGIN_AFILED", f"Attempted Acount No: {account_no}")
        return None
    def withdraw(self,account_no,amount):
        account = self.load_account()
        for acc in account:
           if isinstance(acc,dict) and acc ["account_no"] == account_no: 
             if acc["balanc"] < amount :
                print("The balanc is not enough")
                return acc
             else :
                acc["balanc"] = acc["balanc"] - amount
                file_write = open(self.db_name,"w")
                json.dump(account,file_write,indent=4)
                file_write.close()
                print("Succsseful transeaction! Remainig balance: " + str(acc["balanc"]))
                self.log_event("WITHDRAW", f"Acount No: {account_no}, Amount: {amount}")
                return acc
    def deposit(self,account_no,amount):
        account=self.load_account()
        for acc in account : 
         if isinstance(acc,dict) and acc["account_no"] == account_no:
            print("Welcome to " + acc["customer_name"])
            if amount <=0 :
                print("The amount is not enough")
                return acc
            else:
                acc["balanc"] += amount
                file_write = open(self.db_name , "w")
                json.dump(account,file_write,indent=4)
                file_write.close()
                print("Deposit successful! new balanc: " + str(acc["balanc"]))
                self.log_event("DEPOSIT", f"Acount No: {account_no}, Amount: {amount}")
                return acc
    def create_acount(self,customer_name,pin,initial_balance=0):
        account = self.load_account()
        if len(account) > 0:
            last_account = account[-1]
            new_acc_no = str(int(last_account["account_no"]) + 1)
        else :
            new_acc_no = "1001"
        hashed_pin = self.hash_pin(pin)
        new_account = {
            "account_no": new_acc_no,
            "customer_name": customer_name,
            "balanc": initial_balance,
            "pin": hashed_pin
        }
        account.append(new_account)
        file_write = open(self.db_name, "w")
        json.dump(account,file_write,indent=4)
        file_write.close()
        print("Done, the account number is : " + new_acc_no)
        self.log_event("ACCOUNT_CREATED", f"Acount No: {new_acc_no}, Name: {customer_name}")
        return new_acc_no
    def log_event(self,event_type,details):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{now}] [{event_type}] - {details}\n"
        with open("bank.log", "a", encoding="utf-8") as log_file:
            log_file.write(log_message)
def main():
    atm = BankSystem()
    while True :
        print("1 : Withdraw money\n" , "2 : Deposit money\n" ,"3 : Create a new account\n", "4 : Exite" )
        choice = input("Choice the operation number : ")
        if choice == "1" :
            acc_no = input("Input the accout number : ")
            pin = input("Input the PIN : ")
            if atm.login(acc_no , pin):
                try:
                    amount = float(input("Enter the amount : "))
                    atm.withdraw(acc_no,amount)
                except ValueError:
                            print("Error! you must enter the amount about number only.")
        elif choice == "2" :
            acc_no = input("Input the accout number : ")
            pin = input("Input the PIN : ")
            if atm.login(acc_no , pin):
                try:
                    amount = float(input("Enter the amount : "))
                    atm.deposit(acc_no,amount)
                except ValueError:
                    print("Error! you must enter the amount about number only.")
        elif choice == "3" :
            name = input("Enter your name : ")
            pin = input("Enter the new pin : ")
            try:
                balance = float(input("Enter your balance : "))
            except ValueError:
                print("Please you can use only number.")
                continue
            atm.create_acount(name,pin,balance)
        elif choice == "4" :
            print("You have been successfully logged out and taken out the card, Thhanks for using our bank.")
        else : 
            print("This choice not there, please choice the number from 1 to 3! Thank you.")
if __name__ == "__main__" :
    main()
