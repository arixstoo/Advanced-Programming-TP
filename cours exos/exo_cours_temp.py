
temp = float(input("please enter the temperature : "))

cel= 5 / (9*(temp-32))

print( temp ,  " degrees in fahrenheat = " , round(cel,2) , " degrees in celsius")

if cel < 0 : print("Brr! it's cold in here!")