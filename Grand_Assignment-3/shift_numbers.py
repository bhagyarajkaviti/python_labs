#Given a string, write a program to move all the numbers in it to its end.
#Input
#The input will contain a string A.
#Output
#The output should contain a string after moving all the numbers in it to its end.

string = input()

alphabets = ""
digits = ""

for char in string:
    if char.isalpha():
        alphabets += char
    if char.isdigit():
        digits += char
        
output = alphabets + digits
print(output)