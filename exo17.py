numbers = []
shoe_sizes = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

# Print lists:
print("Numbers:", numbers)
print("Shoe sizes:", shoe_sizes)

numbers.append(3)  
numbers.append(5)  

print("numbers after adding duplicates:",numbers )

# Handle duplicates:
numbers = list(set(numbers))

print("Updated numbers (duplicates removed):", numbers)

combined_list = numbers + shoe_sizes

print("Combined list:", combined_list)