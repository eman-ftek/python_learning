import json
user_profile = {
    "name" : "Eman",
    "role" : "Security Engineer",
    "level" : 5
}
file = open("database.json" , "w")
json.dump(user_profile , file , indent=4)
file.close()
print("We are creat a database successful")
file_read = open("database.json" , "r")
loaded_data = json.load(file_read)
file_read.close()
print("The data has been read \n")
print("The name is : " , loaded_data["name"])
print("The role is : " , loaded_data["role"])
