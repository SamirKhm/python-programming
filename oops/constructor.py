
class Employee:
    
    def __init__(self,salary,name,bond):
        self.salary=salary # create an instance of salary and assgin it to salary
        self.name=name
        self.bond=bond
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of Employee is {self.name} and Salary is {self.salary} with bond of {self.bond} years")
    
e1=Employee(35000,"John Doe",4)
print(e1.get_salary())
print(e1.get_info())