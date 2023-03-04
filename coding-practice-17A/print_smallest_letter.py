#Given a string S, write a program to print the character with the smallest Unicode value in the string S.
string = input()

smallest_char = string[0]
for i in range(1, len(string)):
    if ord(string[i]) < ord(smallest_char):
        smallest_char = string[i]
        
print(smallest_char)