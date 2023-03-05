#Given a number N, write a program that reads N numbers and prints each of the given N numbers by rounding upto 2 decimals on a new line.
n = int(input())

for i in range(n):
    number = float(input())
    print(round(number,2))