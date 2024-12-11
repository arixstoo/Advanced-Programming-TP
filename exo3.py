total = float(input("Enter the total amount of purchase: "))
num = int(input("Enter the number of items: "))
day = input("Enter the day: ")

if day.lower() not in ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Error: Please enter a valid day!")

else:
    total_price = total
    if day.lower() in ["saturday", "sunday"]:
        total_price -= total * 0.2  
        if num > 5:
            total_price -= total * 0.05  
    else:
        if num > 5:
            total_price -= total * 0.05  

    print("Total amount:", total)
    print("Number of items:", num)
    print("Day of the week:", day)
    print("Total price after discount:", total_price)