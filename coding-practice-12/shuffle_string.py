#Given a string and N integers, where N is the length of the string, write a program to print the string after shuffling the characters as per the order of the integers given.
string = input()

length = len(string)
result = ""
for i in range(1, length + 1):
    index = int(input())
    result = result + string[index]
    
print(result)