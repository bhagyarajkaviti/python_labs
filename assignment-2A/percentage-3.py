#write a program that reads a percentage P and a number N and checks if the P percentage of 500 is equal to the number N.
percentage = int(input())
number = int(input())

value = (percentage/100) * 500
value = int(value)

result = (number == value)
print(result)