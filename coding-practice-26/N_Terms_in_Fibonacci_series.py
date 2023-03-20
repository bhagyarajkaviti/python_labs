#Write a program to recursively find the Nth term in the Fibonacci series.
#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8... The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
def fibonacci(n):
    # Complete this function to return nth term in fibonacci series
    if n <= 1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)
def get_fibonacci_series(n):
    # Complete this function to return list of n terms of fibonacci series
    fibonacci_list = []
    for i in range(n):
        fibonacci_list.append(fibonacci(i))
    return fibonacci_list
n = int(input())
# Call the get_fibonacci_series function
result = get_fibonacci_series(n)
print(result)