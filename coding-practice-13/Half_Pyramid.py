#Write a program to print the half pyramid pattern up to the given N number of rows.
n = int(input())

for i in range(1, n + 1):
    output = ""
    for j in range(1, i + 1):
        output = output + str(j) + " "
    print(output)