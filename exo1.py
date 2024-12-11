name = input("Please enter your name : ")
if name.upper()=="VIP":
    print("Enjoy the show for free !")
else:
    tickets = int(input("How many tickets would you like to buy? "))
    print("The total cost is ", tickets*15.50, "DA")
    print("Enjoy your tickets !")    