#Given the number of rows N, write a program to print the hallow half pyramid pattern similar to the pattern shown below.
#   1
#   1  2
#   1     3
#   1       4
#   1  2  3 4  5
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(i)
    elif i == n:
        lastline = ""
        for j in range(1, n +1):
            lastline = lastline + str(j) + " "
        print(lastline)
    else:
        middlelines = ""
        if i >= 2 and i < n:
            middlelines = "1 " + "  " * (i - 2) + str(i)
            print(middlelines)