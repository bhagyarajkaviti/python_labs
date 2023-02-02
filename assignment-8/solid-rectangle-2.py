#Write a program to print a rectangle pattern of M rows and N columns using the plus character ( + ).
#Note: There is a space after each plus + character.
#Note: Use for loop.
rows = int(input())
columns = int(input())

for i in range(rows):
    print("+ " * columns)