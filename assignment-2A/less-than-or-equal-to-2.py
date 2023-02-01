# write a program that reads two numbers  and B and checks,
#   1) If A is less than or equal to B.
#   2) If B is less than or equal to A.
A = int(input())
B = int(input())

result1 = (A <= B)
result1 = str(result1)

print("A <= B is " + result1)

result2 = (B <= A)
result2 = str(result2)

print("B <= A is " + result2)