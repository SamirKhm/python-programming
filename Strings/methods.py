name=" Harry Potter "

length=len(name)
print(length)

# changing case
print(name.lower())
print(name.upper())
print(name.capitalize())

# removing space
print(name.strip())

# find and replace
print(name.find("Potter"))
print(name.replace("H","O"))
print(name)

# splitting and joining

# checking properties
print(name.isdecimal())
n="0.999"
print(n.isdecimal())