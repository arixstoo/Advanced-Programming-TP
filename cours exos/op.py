a = int(input("enter the first num : "))
b = int(input("enter the second num : "))
op = input("enter the operation : ")

if op == "+" : print("a + b = " , a+b )

elif op == "*" : print("a * b = " , a*b )

elif op == "-" : print("a - b = " , a-b )


elif (op != "+")  | (op != "*") | (op != "-")  : 
    print ("Veuillez choisir l'un de ces operateurs : + ou * ou - ")