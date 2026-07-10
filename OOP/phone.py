class phone():
    def __init__(self,owner):
        self.owner=owner
        self.__message= "This is a very secret message!"
    def get_message(self,password):
        if password == "1234":
            return (self.__message)
        else : 
            print("The password is error!")
    def set_message(self,password,new_message):
        if password == "1234":
         self.__message = new_message
         return
        else :
            return("The password error")
owner=input("Enter the owner name : ")
password=input("Enter the password : ")
my_phone=phone(owner)
print(my_phone.get_message("1234"))
print(my_phone.set_message("0000"))
