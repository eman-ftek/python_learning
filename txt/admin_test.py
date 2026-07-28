import json
user_profile = {
    "username" : "Eman Ali",
    "role" : "Admin"
}
file_write = open("system_config.json" , "w")
json.dump(user_profile , file_write , indent=4)
file_write.close()
file_read = open("system_config.json" , "r")
loaded = json.load(file_read)
file_read.close()
if loaded["role"] == "Admin" :
    print("You can accsses")
else :
    print("You can not accsses")
