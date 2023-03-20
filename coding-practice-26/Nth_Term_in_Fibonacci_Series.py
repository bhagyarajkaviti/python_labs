#Write a program to recursively find the Nth term in the Fibonacci series.
#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8... The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)  + fibonacci(n-2)

n = int(input())
result = fibonacci(n)
print(result)
