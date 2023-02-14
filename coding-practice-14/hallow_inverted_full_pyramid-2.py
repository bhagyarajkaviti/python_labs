#Given the number of rows N, write a program to print the hallow inverted full pyramid pattern similar to the pattern shown below.
#   1 2 3 4 5
#    1     4
#     1   3
#      1 2
#       1
n= int(input())

k = n
for i in range(1, n + 1):
    left_space = " " * (i - 1)
    if i >= 2 and i < n:
        hallow_space = "  " * (n - 1 - i)
        print(left_space + "1 " + hallow_space + str(k - 1))
        k = k - 1
    elif i == 1:
        remaining_lines = ""
        for j in range(1, n + 1):
            remaining_lines =  left_space + remaining_lines + str(j) + " "
        print(remaining_lines)
    else:
        print(left_space + "1 ")
        

#
#n = int(input())
#for row in range(1, n+1):
#    i = n - (row -1)
#    left_spaces = " " * (row-1)
#    if (i > 2) and (i < n):
#        hollow_spaces = "  " * (i-2)
#        numbers = "1 " + hollow_spaces + (str(i) + " ") 
#        print(left_spaces + numbers)
#    else:
#        numbers = ""
#        for j in range(1, i+1):
#            numbers = numbers + (str(j) + " ")
#        print(left_spaces + numbers)