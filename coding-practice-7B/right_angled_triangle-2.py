#Write a program that reads a number N and prints a Right Angled Triangle of N rows using numbers starting from 1.
#1
#2 2
#3 3 3
#4 4 4 4 
rows = int(input())

count = 1
while count <= rows:
    print((str(count) + " ") * count)
    count += 1