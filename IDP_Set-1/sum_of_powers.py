#You are given numbers. Each number is concatenated with its power and the power is a single-digit integer.
#Write a program that reads the space-separated numbers and calculates the powers of each number and prints its sum.
#Note
#Sum = X₁pow₁ + X22 + x3 + xpow4 + ... + XNOWN
#Where X is concatenated with pow₁, and pow; is a single-digit integer.
#Input
#The input will be a single line containing space-separated integers representing the numbers.
#Output
#The output should be a single line containing an integer obtained by adding each number multiplied by its power
series = input().split()
summation = 0
for item in series:
    if len(item) > 1:
        number = int(item[:-1])
        power = int(item[-1])
        summation += number ** power
    elif len(item) == 1:
        number = 0
        power = int(item)
        summation += number ** power
print(summation)