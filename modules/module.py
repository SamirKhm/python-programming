'''Two types of Modules
-Built in modules
-External modules
'''
import math
import os
import myModule
import requests
x=math.sqrt(2)
print(x)

myModule.hello()

r=requests.get("https://www.google.com")
print(r.text)