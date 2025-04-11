# UNORDERED

f={"s","a","r","a"}

print(f,type(f))

f.discard("w") # dont show error even if element is not present

f.pop() # removes a randome element

a={1,2,3}
b={4,5,3}
c=a.union(b)
print(c)

d=a.intersection(b) # common element``
print(d)