import json
import hashlib
class SecuritySystem():
    def __init__(self):
        self.db_name = "secure_db.json"
    def hash_code(self,vip_code):
        return hashlib.sha256(vip_code.encode()).hexdigest()
    def save_visitore(self,name,raw_code):
        encrypted_code = self.hash_code(raw_code)
        visitor_data = {
            "visitor_name":name,
            "secure_code":encrypted_code
        }
        file = open(self.db_name , "w")
        json.dump(visitor_data , file , indent=4)
        file.close()
    def read_visitore(self):
        file_read = open(self.db_name , "r")
        data = json.load(file_read)
        file_read.close()
        print("Show data \n")
        print("visitor name : " , data["visitor_name"])
        print("secure_code : " , data["secure_code"])
        
visit = SecuritySystem()
visit.save_visitore("Ali" , "ema12345")
visit.read_visitore()
