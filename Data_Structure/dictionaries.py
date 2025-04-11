d={"name":"Samir","age":23}

print(d)

print(d["name"])
d["age"]=18

print(d)
print(d.keys())
print(d.values())
d.clear()
print(d)

# dictionary comprehension
s={x:x*x for x in range(1,11)}
print(s)