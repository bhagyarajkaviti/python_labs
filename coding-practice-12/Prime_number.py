#Write a program to check whether the given number is a Prime number or not.
#A Prime Number is a number that is divisible only by itself and one.
number = int(input())

factor = 0
for i in range(2, number):
    if number % i == 0:
        factor = factor + 1
if factor == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")