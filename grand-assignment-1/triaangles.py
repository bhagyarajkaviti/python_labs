#Given three sides of the triangle(a, b, c) as input. Write a program to determine whether the triangle is Equilateral, Isosceles or Scalene.
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Equilateral")
elif a == b or b == c or c == a:
    print("Isosceles")
elif a != b != c:
    print("Scalene")