#Write a program to create a menu driven calculator that performs basic arithmetic operations (+, -, *, /, and %).
operator = input()
A = int(input())
B = int(input())

if operator == "+":
    print(A + B)
elif operator == "-":
    print(A - B)
elif operator == "*":
    print(A * B)
elif operator == "/":
    print(A / B)
elif operator == "%":
    print(A % B)