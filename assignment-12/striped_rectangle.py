#Given an integer number M, N as input. Write a program to print a striped rectangular pattern of M rows and N columns using (+ and -) character.
rows = int(input())
columns = int(input())

for i in range(rows):
    if i % 2 == 0:
        print("+ " * columns)
    else:
        print("- " * columns)