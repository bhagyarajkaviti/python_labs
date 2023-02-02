#Given three angles of a triangle, write a program to check whether the triangle is valid or not. A triangle is valid if the sum of its three angles is equal to 180 degrees.
a = int(input())
b = int(input())
c = int(input())

if (a + b + c) == 180:
    print("It's a Triangle")
else:
    print("It's not a Triangle")