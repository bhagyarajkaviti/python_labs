#Write a program that reas a string and a number N and checks if the first N characters of the string and the last N characters of the string are not the same.
string = input()
number = int(input())

result = (string[:number] != string[len(string) - number:])

print(result)