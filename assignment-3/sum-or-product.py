#Write a program that reads two numbers A and B and checks if the sum of A and B is less than 10.
#Print the sum of A and B if the sum of A and B is less than 10. Otherwise, print the product of A and B.
A = int(input())
B = int(input())

if (A + B) < 10:
    print(A + B)
else:
    print(A * B)