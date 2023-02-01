#write a program that reads two numbers A and B and checks if the A is greater than B. Print the result as shown in the sample output.
number1 = int(input())
number2 = int(input())
result = (number1 > number2)
result = str(result)
print("A > B is " + result)