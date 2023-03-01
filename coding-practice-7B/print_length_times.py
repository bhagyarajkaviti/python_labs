#Write a program that reads a string and prints the first character of the given string on N lines, where N is the length of the given string.
string = input()
n = len(string)

count = 0
while count < n:
    print(string[0])
    count += 1