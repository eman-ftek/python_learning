import json
task_data = {
    "task_name" : "Check network ports" , 
    "status" : "pending"
    }
file_write = open("my_taske.json" , "w")
json.dump(task_data , file_write , indent=4)
file_write.close()
print("The task are saved insid the file .")
print(type(task_data))
file_read = open("my_taske.json" , "r")
loaded = json.load(file_read)
file_read.close()
print(type(loaded))
print("task_name : " , loaded["task_name"])
print("status : " , loaded["status"])