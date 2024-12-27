unique_words = set()

total_words = 0

# Function to save to a file
def save_to_file(words):
    file_path = input("Enter the path to save the file: ")
    with open(file_path, "w") as file:
        for word in sorted(words):
            file.write(word + "\n")
    print(f"Unique words saved to {file_path}.")

#Main:
while True:
    word = input("Enter a word: ").strip().lower()

    total_words += 1 

    if word in unique_words:
        print(f"Duplicate word found! You entered {total_words} words in total.")
        print(f"Total unique words: {len(unique_words)}")
        print("Unique words (alphabetically):")
        for w in sorted(unique_words):
            print(w)
        save = input("Do you want to save the unique words to a file? (y/n): ").strip().lower()
        if save == 'y':
            save_to_file(unique_words)
        break
    else:
        # Add the word to the set of unique words
        unique_words.add(word)