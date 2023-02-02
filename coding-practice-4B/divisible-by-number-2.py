#Write a program that reads a number N and checks if the triple of N is divisible by 6.
#Print the triple of N if the triple of N is divisible by 6. Otherwise, print N .
N = int(input())

condition = (3 * N) % 6 == 0

if condition:
    print(N * 3)
else:
    print(N)