# Decorator is a function that takes a function , it 
# creates a new function inside its body (wrapper) . Then it returns that new function

def decorator(func):
    def wrapper():
        print("I am about to axecute a function")
        func()
        print("I have printed this function")
    return wrapper

@decorator    # skip 18-19-20 line code
def say_hello():
    print("Hello")


say_hello()

# new function is returned and stored in f
# f=decorator(say_hello)
# f()

'''
f will look like this
print("I am about to execute a function")
print("Hello")
print"I have executed this function")
'''