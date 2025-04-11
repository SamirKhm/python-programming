try:
    f=open("samir.txt","r")
    # default rt
    for line in f:
        print(line)

    
    f.close()
    
except Exception as e:
    print("File not found")
