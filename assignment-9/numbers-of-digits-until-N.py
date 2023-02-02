#Given an integer N, write a program that prints the count of the total number of digits between 1 and N.
n =int(input())

count = 0
for i in range(1, n+1):
    count += len(str(i))

print(count)
