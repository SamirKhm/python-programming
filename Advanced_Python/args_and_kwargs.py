def sum(*args):
    # args will be a tuple of all 
    # values passed to sum
    print(args)
    sum=0
    for i in args:
        sum+=i
    return sum
    
print(sum(3,2,4,4,4,4,3))

def marks(**kwargs):
    # kwargs is a dictionary with all the key 
    # value pairs which is passed to marks
    for i in kwargs.keys():
        print(f"The marks of {i} are {kwargs[i]}")
        
marks(shubham=34,vikrant=35,jack=56)

# COMBINED
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    
func(1,2,3,4,5,6,7,Marry=12)