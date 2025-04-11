class Animal:
    location="India"
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print("Speaking now ...")
        
class Dog(Animal):
    
    def speak(self):
        super().speak() # caling method of super class
        print("Woof.")
        
a=Animal("Dog")
a.speak()     

d=Dog("Bruno")
d.speak()
