#You are given a string S as input, write a program to print the string after reversing the words of the given sentence.
string = input()

string_list = string.split()
reverse_list = string_list[::-1]
output = ""
for i in reverse_list:
    output += i + " "
print(output)