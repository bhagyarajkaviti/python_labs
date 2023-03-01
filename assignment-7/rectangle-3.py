#Write a program that reads two numbers M and N, and prints a Rectangle of M rows and N columns using the numbers from 1 as shown in the sample output.
#1 1 1 1 
#2 2 2 2 
#3 3 3 3 
rows = int(input())
columns = int(input())

count = 1
while count <= rows:
    print((str(count) + " ") * columns)
    count += 1