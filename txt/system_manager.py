import hashlib
class User():
    def __init__(self, username,password):
        self.username = username
        self.password = self.hash_password(password)
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    def save_user(self):
        file = open("user_db.txt" , 'a')
        file.write(self.username + " : /" + self.password + "\n")
        file.close()
name = input("Enter your name : ")
password = input("Enter your password : ")
user = User(name,password)
user.save_user()
file = open("user_db.txt" , 'r')
print(file.read())
file.close()
