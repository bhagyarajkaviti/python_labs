#Given a number N, write a program to print the letter M of N rows with two Solid Pyramids using zeros ( 0 ) and dots ( . ).
#. . . 0 . . . . . . 0 . . .
#. . 0 0 0 . . . . 0 0 0 . .
#. 0 0 0 0 0 . . 0 0 0 0 0 .
#0 0 0 0 0 0 0 0 0 0 0 0 0 0 
n = int(input())

for i in range(1, n + 1):
    side_dots = ". "* (n - i)
    center_dots = ". " * (n - i) * 2
    zeros = "0 " * (2*i - 1)
    print(side_dots + zeros + center_dots + zeros + side_dots)