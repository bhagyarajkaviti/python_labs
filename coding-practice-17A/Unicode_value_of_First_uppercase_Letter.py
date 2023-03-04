#Given a string S, write a program to print the Unicode value of the first uppercase character in the string S.
string = input()

for char in string:
    if char == char.upper():
        Unicode = ord(char)
        print(Unicode)
        break