numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input("Enter an index (or -1 to stop): "))
    
    if index == -1:
        break
    
    if 0 <= index < len(numbers):

        new_value = int(input("Enter the new value: "))
        
        numbers[index] = new_value
        
        print("Updated list: ", numbers)
    else:
        print("Invalid index. Please try again.")

print("Final list: ", numbers)