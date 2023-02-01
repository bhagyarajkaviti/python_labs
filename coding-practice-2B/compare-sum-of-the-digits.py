#Write a program that reads a two digit number N. The N consists of only two digits. Check if the sum of the digits of N is greater than 7.
number = int(input())
number = str(number)
digit1 = int(number[0])
digit2 = int(number[1])
result = ((digit1 + digit2) > 7)
#result = ((int(number[0]) + int(number[1])) > 7)
print(result)