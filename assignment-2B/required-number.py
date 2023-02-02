#Write a program that reads a number N and checks if the number N is between 50 and 100 or if the first digit of N is equal to 7.
number = int(input())
A = str(number)

condition1 = (number > 50 and number < 100)
condition2 = (int(A[0]) == 7)

result = condition1 or condition2
print(result)