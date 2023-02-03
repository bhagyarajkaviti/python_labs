#Write a program to check if a number N is an armstrong number or not.
#A N-digit number is called armstrong number if the number is equal to the sum of the Nth power of its digits.
n = int(input())
n_string = str(n)
l = len(n_string)

sum = 0
for i in n_string:
    sum += int(i) ** l

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")