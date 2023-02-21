#Given N inputs, write a program to print the first negative number.
n = int(input())

for i in range(n):
    number = int(input())
    if number < 0:
        print(number)
        break