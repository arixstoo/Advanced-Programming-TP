def print_numbers_excluding_zero():
    try:
        user_input = input("Please enter a positive integer: ")
        if not user_input.isdigit():
            raise ValueError("Input must be a positive integer.")
        n = int(user_input)
        if n <= 0:
            raise ValueError("The number must be positive.")
        for i in range(-n, n + 1):
            if i != 0:
                print(i)
    except ValueError as e:
        print(f"Invalid input: {e}")

print_numbers_excluding_zero()