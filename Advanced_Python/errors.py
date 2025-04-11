# try:
#      a=int(input("Enter number 1 : "))        
#      b=int(input("Enter number 2 : "))

#      print(f"Sum is {a+b}")

# except ValueError:
#     print("Value error")

# except Exception as err:
#     print(f"Error Occured\nError : {err}")

a=int(input("Enter number 1 : "))        
b=int(input("Enter number 2 : "))

if b==0:
    raise ValueError("Please dont divide by Zero") # throw error

print(f"Result : {a/b}")
