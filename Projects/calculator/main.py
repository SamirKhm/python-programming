while True:
    try:
        print("A Simple Calculator\n")
        a=int(input("Enter the first number : "));
        b=int(input("Enter the second number : "));
        
        print("What kind of operation do you want to perform. Press + for addition\nPress - for substraction\nPress / for division\nPress * for multiplication")
        
        o=input("Enter Operaion : ");
        
        match o:
            case "+":
                print(f"The sum of {a} and {b} is : {a+b}");
            case "-":
                print(f"The result of substraction of {a} and {b} is : {a-b}");
            case "*":
                print(f"The result of multiplication of {a} and {b} is : {a*b}");
            case "/":
                print(f"The result of division of {a} and {b} is : {a/b}");           
        
        a=input("Do you want to procced(y/n) : ")
        
        if(a=="n"):
            break
        
    except Exception as e:
        print("Error : ",e);
    