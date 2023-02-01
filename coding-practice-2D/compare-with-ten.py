#write a program that reads two numbers A and B and check if any one of the below conditions is satisfied.
#   The sum os A and B is less than 10.
#   The differance between A and B is less than 10.
#   A is between 5 and 30.
number1 = int(input())
number2 = int(input())

check_condition1 = ((number1 + number2) < 10)
check_condition2 = ((number1 - number2) < 10)
check_condition3 = (number1 > 5) and (number1 < 30)

result = check_condition1 or check_condition2 or check_condition3
print (result)