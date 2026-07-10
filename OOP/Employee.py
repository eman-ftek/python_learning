class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def calculate_salary(self) :
        return self.base_salary
class Manager(Employee):
    def add_bonus(self,amount):
        self.amount=amount
    def calculate_manager_salary(self):    
        total_salary=self.base_salary+self.amount
        return total_salary   
m_name=input("Enter the manager name :")
m_salary=int(input("Enter the salary :"))
m_bouns=int(input("Enter the bouns :"))
salary= Manager(m_name, m_salary)
salary.add_bonus(m_bouns)
total= salary.calculate_manager_salary()
print("The total salary is : " + str(total))
