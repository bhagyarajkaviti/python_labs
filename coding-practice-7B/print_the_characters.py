#Write a program that reads a string and prints each character of the given string on a new line.
string = input()
n = len(string)

count = 0
while count < n:
    print(string[count])
    count += 1