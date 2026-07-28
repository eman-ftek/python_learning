import json
import hashlib
class Security:
    def __init__(self):
        self.db_name = "secure_db.json"
    def hash_code(self,vip_code):
        return hashlib.sha256(vip_code.encode()).hexdigest()
    def save_visitor(self,name,raw_code):
        data = []
        try :
         file_read = open(self.db_name , "r")
         data = json.load(file_read)
         print(type(data))
         file.close()
        except:
            pass
        encrypted_code = self.hash_code(raw_code)
        visitore_data = {
         "visitore_name" : name,
         "secure_code" : encrypted_code
         }
        data.append(visitore_data)
        file_write = open(self.db_name , "w")
        json.dump(data , file_write , indent=4)
        file_write.close()
        print("Seccess")
    def read_visitore(self):
        try:
         file_read = open(self.db_name , "r")
         data = json.load(file_read)
         for visitor in data:
             print("visitor_name : " , visitor["visitore_name"])
             print("secure_coda : " , visitor["secure_code"])
        except Exception as e:
          print("The database now is impyte or hapen error will read")
visit = Security()
visit.save_visitor("Emam" , "123654mmm")
visit.save_visitor("feem" , "456321mk")
visit.save_visitor("Alo" , "mnb123m")
visit.read_visitore()
