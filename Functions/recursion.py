

def fib(i):
    #Base case
    if(i==0 or i==1):
        return i
    
    return fib(i-2) + fib(i-1)

term=5
for i in range(0,term):
    print(fib(i))