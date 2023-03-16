#Write a program to recursively compute the value of A raised to the power B.
def calculate_power(x, y):
    if y == 1: # Base case
        return x
    else:
        y -= 1
        return x * calculate_power(x, y)    # Recursion

a = int(input())
b = int(input())
# Call the calculate_power function
result = calculate_power(a, b)
print(result)