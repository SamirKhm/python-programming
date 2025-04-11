from functools import reduce
# map,filter,reduce - higher order function

# MAP
n=[1,2,4,6,7,8,12]

def sqaure(x):
    return x*x;

new_n =list(map(sqaure,n))
print(new_n)

new_n=list(map(lambda x:x*x,n))
print(new_n)
# FILTER
def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
    
a=[1,12,32,45,65,2,34,98,2,3,4,5,6]

new=filter(is_greater_than_9,a)
print(list(new))

new=list(filter(lambda x:x>9,a))
print(list(new))
    

# REDUCE

a=[1,2,3,4,5,6]

# reduces array to a single number by performing the action which 
# is sum here

def sum(a,b):
    return a+b

c=reduce(sum, a)
print(c)