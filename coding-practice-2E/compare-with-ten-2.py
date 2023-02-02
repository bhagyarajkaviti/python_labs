#Write a program that reads three numbers A, B, and C, and checks if the sum of any two numbers is always greater than 10.
A = int(input())
B = int(input())
C = int(input())

sum1 = A + B > 10
sum2 = B + C > 10
sum3 = C + A > 10

result = (sum1) and (sum2) and (sum3)
print(result)