#Given an integer N, write a program which reads N inputs and prints the sum of the given input integers.
integer = int(input())

count = 0
b = 0
while count < integer:
    a = int(input())
    b = b + a
    count = count + 1
print(b)