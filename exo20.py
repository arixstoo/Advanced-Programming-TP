import statistics

user_list = []

def save_to_file(list):
    file_path = input("Enter the path to save the file: ")
    with open(file_path, "w") as file:
        for num in sorted(list):
            file.write(str(num) + "\n")
    print(f"List saved to {file_path}.")

number = int(input("Enter a number (0 to stop): "))

while True:
    if number == 0:
        break
    else:
        user_list.append(number)
        
        print("Current list:", user_list)
        
        sorted_list = sorted(user_list)
        print("Sorted list:", sorted_list)
        
        sorted_list.reverse() 
        print("List in descending order:", sorted_list)
        
        number = int(input("Enter a number (0 to stop): "))


print("List mean:", statistics.mean(user_list))
print("List median:", statistics.median(user_list))

save = input("Do you want to save the list to a file (y/n): ")
if save == 'y':
    save_to_file(user_list)
else:
    exit()