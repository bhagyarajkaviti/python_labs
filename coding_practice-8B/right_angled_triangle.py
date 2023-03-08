#Write a program that reads a number N and prints a Right Angled Triangle of N rows using stars ( * ).
n = int(input())

for i in range(1, n+1):
    print("*" * i)