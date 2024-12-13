try:
    width = int(input("Width: ").strip()) 
    height = int(input("Height: ").strip()) 
    if width > 0 and height > 0:
        for _ in range(height):
            print("#" * width)  
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")