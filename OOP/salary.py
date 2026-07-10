class Employee():
    def __init__(self,name):
        self.name=name
    def get_salary(self):
        salary=5000
        return salary
class Manager(Employee):
    def get_salary(self):
        total_salary=super().get_salary() + 2000
        return total_salary
name=input("Emter the employee name :")
emp=Employee(name)
mgr=Manager(name)
print("The Employee" + name, " salary is " + str(emp.get_salary()))
print("The Manager salary is " + str(mgr.get_salary()))
