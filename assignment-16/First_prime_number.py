#You are given N inputs. Write a program to print the first prime number in the given inputs.
n = int(input())

for i in range(1, n+1):
    number = int(input())
    factor = 0
    for j in range(1, number):
        if number % j == 0:
            factor = factor + 1
    if factor == 1:
        print(number)
        break