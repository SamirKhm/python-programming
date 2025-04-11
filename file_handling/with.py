# f=open("samir.txt","r")
# print(content:=f.read())
# f.close()

with open("samir.txt","r") as f:
    print(content:=f.read())
    
    # no need to wrtie f.close() 
    # file is already closed by default when using eith syntax
    
    