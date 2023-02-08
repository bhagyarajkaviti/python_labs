#Given an integer between 0 and 10000, write a program to print the sum of its digits.
number = int(input())
number_string = str(number)
l = len(number_string)

if l ==1:
    summ = int(number_string[0])
elif l == 2:
    summ = int(number_string[0]) + int(number_string[1])
elif l == 3:
    summ = int(number_string[0]) + int(number_string[1]) + int(number_string[2])
elif l == 4:
    summ = int(number_string[0]) + int(number_string[1]) + int(number_string[2]) + int(number_string[3])
elif l == 5:
    summ = int(number_string[0]) + int(number_string[1]) + int(number_string[2]) + int(number_string[3]) + int(number_string[4])

print(summ)