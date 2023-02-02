#Write a program that reads two sides A and B of a right- angled triangle and prints the Hypotenuse H of the right-angled triangle.
A = int(input())
B = int(input())

Hypotenuse = int(((A ** 2) + (B ** 2)) ** 0.5)

print(Hypotenuse)