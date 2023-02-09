#Write a program to print the numbers in the given N number of rows in the following half pyramid pattern.
#    1
#    23
#    456
#    7 8 9 10
#    11 12 13 14 15
n = int(input())

number = 1

for i in range(1,n +1):
    output = ""
    for j in range(i):
        output = output + str(number) + " "
        number = number + 1
    print(output)