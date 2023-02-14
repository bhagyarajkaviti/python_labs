#Given the number of rows N, write a program to print the hallow inverted half pyramid pattern similar to the pattern shown below.
#   1 2 3 4 5
#   1     4
#   1   3
#   1 2
#   1
n = int(input())

k = n
for i in range(1, n + 1):
    if i == 1:
        firstline = ""
        for j in range(1, n + 1):
            firstline = firstline + str(j) + " "
        print(firstline)
    elif i >= 2 and i < n:
        middlelines = "1 " + "  " * (n - 1 - i) + str(k - 1)
        k = k - 1
        print(middlelines)
    else:
        print("1")
        
        
        
#
#n = int(input())
#
#for i in range(n, 0, -1):
#    if (i > 2) and (i < n):
#        hollow_spaces = "  " * (i - 2)
#        numbers = "1 " + hollow_spaces + (str(i) + " ")
#        print(numbers)
#    else:
#        numbers = ""
#        for j in range(1, i+1):
#            numbers = numbers + (str(j) + " ")
#        print(numbers)