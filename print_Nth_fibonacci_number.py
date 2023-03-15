# Given an integer N. Write a program to print Nth fibonacci number of the series.
def fibonacci(n):
    #if n == 0:
    #    return 0
    #if n == 1:
    #    return 1
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input())
result = fibonacci(num)
print(result)