#Write a program that reads a number N and checks if one of the given conditions is satisfied.
    #N is divisible by 5 and N is divisible by 7.
    #N is less than 7.
#Print N if one of the given conditions is satisfied. Otherwise, print the remainder when N is divided by 5 and the remainder when N is divided by 7 on each line.
number = int(input())

condition1 = number % 5 == 0 and number % 7 == 0
condition2 = number < 7

if condition1 or condition2:
    print(number)
else:
    print(number % 5)
    print(number % 7)