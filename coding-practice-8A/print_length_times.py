#Write a program that reads a string and prints the first character (The character at index O) of the given string on N lines, where N is the length of the given string.
string = input()
n = len(string)

for i in range(n):
    print(string[0])