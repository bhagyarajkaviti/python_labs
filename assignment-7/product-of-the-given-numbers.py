#Given an integer N, write a program which reads N inputs and prints the product of the given input integers.
n = int(input())

count = 1
sum = 1
while count <= n:
    number = int(input())
    count = count + 1
    sum = sum * number
print(sum)
    