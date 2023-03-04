#Given a string S, write a program to print the Unicode values of all the characters in S, each on a new line.
string = input()
for char in string:
    print(ord(char))