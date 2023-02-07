#Write a program to print a rectangle pattern of M rows and N columns using the characters as shown below.
rows = int(input())
columns = int(input())

for i in range(1, rows+3):
    if i == 1 or i == rows +2:
        print("+" + "-" *(columns) + "+")
    else:
        print("|" + " " *(columns) + "|")