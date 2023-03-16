#Write a program to recursively compute the factorial of a given number N.
#Factorial is the product of all positive integers less than or equal to N.
def compute_factorial(n):
    # Complete this recursive function
    if n <= 0:
        return 1
    #if n == 1:
    #    return 1
    #if n == 0:
    #    return 1
    return (n * compute_factorial(n - 1))

num = int(input())
# Call the compute_factorial function
result = compute_factorial(num)
print(result)