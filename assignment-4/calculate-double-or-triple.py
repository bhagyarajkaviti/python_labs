#Write a program that reads a number N and checks if N is divisible by 3.
#Print the triple of N if N is divisible by 3. Otherwise, print the double of N.
number = int(input())

if number % 3 == 0:
    print(3 * number)
else:
    print(2 * number)