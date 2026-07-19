import hashlib
class Visitor():
    def __init__(self,name,vip_code):
        self.name = name
        self.vip_code = self.hash_vip_code(vip_code)
    def hash_vip_code(self,vip_code):
        return hashlib.sha256(vip_code.encode()).hexdigest()
    def save_visitor(self):
       visit= open("visitor.txt" , "a") 
       visit.write(self.name + ":" + self.vip_code + "\n")
       visit.close()
name = input("Enter your name : ")
vip_code = input('Enter your code : ')
visitor = Visitor(name,vip_code)
visitor.save_visitor()
reader = open("visitor.txt" , "r")
print(reader.read())
reader.close()
