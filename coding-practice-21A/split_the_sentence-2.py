#Given a list of N words, write a program to print each word in a line.
string = input()
string_list = string.split(" ")

for word in string_list:
    print(word)