import random as rn

num = rn.randint(0 , 100)
guess = int(input("enter your guess : "))
compt=1

while guess != num :
    if guess>num :
        print ("The number is less than " , guess)
    
    if guess<num :
        print ("The number is greater than " , guess)

    guess = int(input("enter your guess : "))
    compt=compt+1

print("you win !!")
print("you needed " , compt , "try to find te number")