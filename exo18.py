numbers = [1, 2, 3, 4, 5]

# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Sort the list")
    print("6. Reverse the list")
    print("7. Search for an element")
    print("8. Save the list to a file")
    print("9. Load the list from a file")
    print("10. Quit")

# Function to append an element to the list
def append_element():
    element = int(input("Enter the element to append: "))
    numbers.append(element)
    print("Updated list:", numbers)

# Function to insert an element at a specific position
def insert_element():
    index = int(input("Enter the index position: "))
    element = int(input("Enter the element to insert: "))
    if 0 <= index <= len(numbers):
        numbers.insert(index, element)
        print("Updated list:", numbers)
    else:
        print("Invalid index.")

# Function to pop an element from the list
def pop_element():
    if numbers:
        popped_element = numbers.pop()
        print(f"Popped element: {popped_element}")
        print("Updated list:", numbers)
    else:
        print("The list is empty.")

# Function to remove an element from the list
def remove_element():
    element = int(input("Enter the element to remove: "))
    if element in numbers:
        numbers.remove(element)
        print(f"Removed element: {element}")
        print("Updated list:", numbers)
    else:
        print(f"{element} not found in the list.")

# Function to sort the list
def sort_list():
    numbers.sort()
    print("List sorted:", numbers)

# Function to reverse the list
def reverse_list():
    numbers.reverse()
    print("List reversed:", numbers)

# Function to search for an element in the list
def search_element():
    element = int(input("Enter the element to search for: "))
    if element in numbers:
        index = numbers.index(element)  # Find the index of the element
        print(f"{element} found at index {index}.")
    else:
        print(f"{element} not found in the list.")

# Function to save the list to a file
def save_list():
    with open("numbers_list.txt", "w") as file:
        for item in numbers:
            file.write(str(item) + "\n")
    print("List saved to 'numbers_list.txt'.")

# Function to load the list from a user-specified file path
def load_list():
    file_path = input("Enter the full path of the file to load: ")
    try:
        with open(file_path, "r") as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        print("File not found at the specified path!")
        return []
    except ValueError:
        print("Error: The file contains invalid data.")
        return []

#Main:
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        append_element()
    elif choice == '2':
        insert_element()
    elif choice == '3':
        pop_element()
    elif choice == '4':
        remove_element()
    elif choice == '5':
        sort_list()
    elif choice == '6':
        reverse_list()
    elif choice == '7':
        search_element()
    elif choice == '8':
        save_list()
    elif choice == '9':
        numbers = load_list()
        if numbers:
            print("List loaded from file:", numbers)
    elif choice == '10':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")