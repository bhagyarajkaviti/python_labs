#Given an integer N as input, write a program to print a number diamond of 2*N -1 rows as shown below.
#Note: There is a space after each number.
#       1
#      1 2
#     1 2 3
#    1 2 3 4
#   1 2 3 4 5
#    1 2 3 4
#     1 2 3
#      1 2
#       1
n = int(input())

for i in range(1, n + 1):
    left_spaces = " " * (n - i)
    number = ""
    for j in range(1, i + 1):
        number = number + str(j) + " "
    print(left_spaces + number)

for k in range(1, n): # inveted full pyramid part
    left_spaces = " " * k
    number = ""
    for b in range(1, n + 1 - k):
        number = number + str(b) + " "
    print(left_spaces + number)
    
#  another solution for INVERTED FULL PYRAMID PART CODE is written below
#for i in range(n - 1, 0, -1):
#    left_space = " " * (n - i)
#    pattern = ""
#    for j in range(1,i+1):
#        pattern = pattern + (str(j)+" ")
#        j = j + 1 
#    print(left_space + pattern)