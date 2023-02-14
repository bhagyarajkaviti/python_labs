#Given the number of rows N, write a program to print the full pyramid pattern similar to the pattern shown below.
#    1
#   1 2
#  1 2 3
# 1 2 3 4
#1 2 3 4 5
n = int(input())


for i in range(1, n + 1):
    output = " " * (n - i)
    for j in range(1, i + 1):
        output = output + str(j) + " "
    print(output)
    