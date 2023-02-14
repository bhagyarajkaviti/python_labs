#Given the number of rows N, write a program to print the inverted full pyramid pattern similar to the pattern shown below.
#   1 2 3 4 5
#    1 2 3 4
#     1 2 3
#      1 2
#       1
n = int(input())

for i in range(n):
    output = ""
    left_space = " " * i
    for j in range(1 , n + 1 - i):
        output = output + str(j) + " "
    print(left_space + output)    