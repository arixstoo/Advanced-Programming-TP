houma=int(input("enter the number of goals scored by 'EL Houma' "))
brania=int(input("enter the number of goals scored by 'EL Berania' "))

if (houma < 0 ) | (brania<0) : print ("kfh score negatif ?")
else :
    if houma == brania : print("it was a tie")
    elif houma>brania : print("'EL Houma wins'")
    else : print("'EL Berania wins'")
