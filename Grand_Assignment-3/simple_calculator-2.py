#Write a program to create a menu-driven calculator that performs basic arithmetic operations (+, -, *, /, and %).
#Input
#The input will be a single line containing two integers and operator(+, -,*,/, and %) similar to 3 + 5.
#Output
#If the given operator is "+", print the sum of two numbers.
#If the given operator is "-", print the result of the subtraction of the two numbers.
#If the given operator is "*", print the multiplication of the two numbers.
#If the given operator is "/", print the result of the division of the two numbers.
#If the given operator is "%", print the result of the modulus operation of the two numbers.

series_list = input().split(" ")

operator = series_list[1]
series_list.remove(operator)
first_num, second_num = [int(i) for i in series_list]

if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "/":
    print(first_num / second_num)
elif operator == "%":
    print(first_num % second_num)

