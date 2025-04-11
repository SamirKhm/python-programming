
class Employee:
    company="ASUS" # This is class attribute
    def __init__(self,salary,name,bond,company):
        self.salary=salary # create an instance of salary and assgin it to salary
        self.name=name
        self.bond=bond
        self.company=company
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of Employee is {self.name} and Salary is {self.salary} with bond of {self.bond} years")
    
e1=Employee(35000,"John Doe",4,"Tesla")
print(e1.company) # Always print instance attribute
print(e1.get_salary())
print(e1.get_info())
print(Employee.company) # This will always print class attribute
# Object Instrospection
# print(dir(e1))