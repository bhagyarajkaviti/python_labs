#Write a program to print a rectangle pattern of M rows and N columns using the plus character ( + ).
#Note: There is a space after each plus + character.
rows = int(input())
columns = int(input())

count = 0
while count < rows:
    print("+ " * columns)
    count = count + 1