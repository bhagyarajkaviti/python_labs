#write a program that reads a two-digit number N and checks,
#   1) If the number N is greater than 25.
#   2) If the first digit of N is greater than the second digit of N.
#Print the result as shown in sample output.
number = int(input())
number = str(number)

result1 = (int(number) > 25)
print(result1)

result2 = (int(number[0]) > int(number[1]))
print(result2)