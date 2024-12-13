try:
    width = int(input("Width: ").strip()) 
    if width > 0:
        print("#" * width)  
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
