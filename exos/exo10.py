import sys
word = input("Enter a word to check if it's a palindrome: ").strip().lower()
if not word:
    print("You didin't enter a word !")
    sys.exit()

is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:  
        is_palindrome = False
        break 

if is_palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
