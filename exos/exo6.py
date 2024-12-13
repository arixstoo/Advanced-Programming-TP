price = float(input("enter the price : "))

dinar = int( price ) 
centime = round((price - dinar)*100)

print("Dinars : " , dinar)
print("centimes : " , centime)