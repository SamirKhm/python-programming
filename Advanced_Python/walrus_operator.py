def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

# a=very_slow_func()
if((a:=very_slow_func())>10):
    print(a)
else:
    print("It's not greater than 10")
    
while(data:=input("Enter value : ")):
    print(data)
    if data=='q':
        break    
    

'''
walrus operator => :=

'''