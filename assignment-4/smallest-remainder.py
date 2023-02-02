#Write a program that reads two numbers A and B and finds the,
    # Remainder when A is divided by B (A%B).
    #Remainder when B is divided by A (B% A).
#Print the smallest among the remainders A % B and B % A.
a = int(input())
b = int(input())

remainder1 = a % b
remainder2 = b % a

if remainder1 < remainder2:
    print(remainder1)
else:
    print(remainder2)