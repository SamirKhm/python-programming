class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    # Instance method        
    def get_info(self):
        print(f"The name is {self.name} and salary is {self.salary}")

    # static method    
    @staticmethod # doesn't need self
    def sum(a,b):
        return a+b    

    @classmethod
    def print_company(cls):
        print(cls.company)
        
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
        
        
e1=Employee("Samir",12000)
e2=Employee("Rohan",14000)
print(Employee.company)

e1.get_info()
e2.get_info()
print(e2.sum(5,4)) # self is the first   argument (ALWAYS)

print(Employee.company)
e1.change_company("Infosys")
print(Employee.company)




