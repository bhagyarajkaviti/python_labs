#Write a program that reads two sides A and B of a right- angled triangle and prints the Hypotenuse H of the right-angled triangle.
#Note:
    #To calculate the Square Root of a number N, use the N power 0.5 (Nº.5).
a = int(input())
b = int(input())

condition = (a ** 0.5) == b

if condition:
    print("Square root of A is equal to B")
else:
    print("Square root of A is not equal to B")