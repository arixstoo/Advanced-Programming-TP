user_input = input("Please type in a string: ")

frame_width = 30

word_length = len(user_input)
left_padding = (frame_width - word_length) // 2
right_padding = frame_width - word_length - left_padding

print("*" * frame_width)
print("*" + " " * (frame_width - 2) + "*")
print("*" + " " * left_padding + user_input + " " * (right_padding-2) + "*")
print("*" + " " * (frame_width - 2) + "*")
print("*" * frame_width)
