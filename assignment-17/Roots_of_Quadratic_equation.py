#You are given cofficients a, b and c of a quadratic equation ax² + bx + c = 0. Find the roots r1 r2 of the equation.
#Note: r1 and r2 should be rounded upto 2 decimal places.

a = int(input())
b = int(input())
c = int(input())

r1 = (- b + (b ** 2 - 4*a*c) ** 0.5)/(2*a)
r1 = round(r1,2)
print(r1)

r2 = (- b - (b ** 2 - 4*a*c) ** 0.5)/(2*a)
r2 = round(r2,2)
print(r2)