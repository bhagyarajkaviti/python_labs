#You are given a string S. Write a program to replace each letter of the string with the next letter that comes in the English alphabet.
#Note: Ensure that while replacing the letters, uppercase should be replaced with uppercase letters, and lowercase should be replaced with lowercase letters.
input_string = input()


output = ""
for char in input_string:
    char_unicode = ord(char)
    next_letter = chr(char_unicode + 1)
    if char == " ":
        next_letter = " "
    output = output + next_letter
print(output)