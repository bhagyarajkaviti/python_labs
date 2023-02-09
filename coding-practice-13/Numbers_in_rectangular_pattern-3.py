#Write a program to print the numbers in the given M number of rows and N number of columns in the following rectangular pattern.
#        1 2 3
#        4 5 6
rows = int(input())
columns = int(input())

number = 1
for i in range(rows):
    output = ""
    for j in range(columns):
        output = output + str(number) + " "
        number = number + 1
    print(output)