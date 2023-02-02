#Write a program that reads three numbers A, B, and C, and prints the greatest number among the three given numbers.
a = int(input())
b = int(input())
c = int(input())

if a > b:
    print(a)
elif b > c:
    print(b)
else:
    print(c)