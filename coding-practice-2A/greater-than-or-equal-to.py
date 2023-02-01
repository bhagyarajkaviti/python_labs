#Write a program that reads two numbers A and B and checks if A is greater than or equal to B. print the result as shown in the sample output.
number1 = float(input())
number2 = float(input())
result = (number1 >= number2)
result = str(result)
print("A >= B is " + result)