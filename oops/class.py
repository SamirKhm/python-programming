
# object is an instance of a class(template) Eg. form with contains the data of John Doe

class Employee:
    company="HP"
    
    def get_salary(self):
        print(self)
        return 35000
    # self is important here , IT IS REFERENCE TO OBJECT(e1,e2)
    
e1=Employee() # object of employee class is created
print(e1.get_salary()) # employee e's get salary is called

e2=Employee()
print(e2.get_salary())
