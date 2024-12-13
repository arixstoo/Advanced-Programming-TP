user_input = input("Please type in a string (lower-case): ")

vowels = ['a', 'e', 'o']

for vowel in vowels:
    if vowel in user_input:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
