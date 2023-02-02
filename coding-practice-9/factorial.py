#Write a program to print the factorial of N. 
#Factorial is the product of all positive integers less than or equal to N.
n = int(input())

multiplication = 1
for i in range(n):
    A = n -i
    multiplication = multiplication * A 
print(multiplication)