#Given an integer value N, write a program to print a number diamond of 2*N -1 rows as shown below.
#   . . . . 0 . . . .
#   . . . 0 0 0 . . .
#   . . 0 0 0 0 0 . .
#   . 0 0 0 0 0 0 0 .
#   0 0 0 0 0 0 0 0 0
#   . 0 0 0 0 0 0 0 .
#   . . 0 0 0 0 0 . .
#   . . . 0 0 0 . . . 
#   . . . . 0 . . . .
n = int(input())

for i in range(1, n + 1):   #Upper part of the Diamond
    dots = ". " * (n - i)
    zeros = "0 " * (2 * i - 1)
    row = dots + zeros + dots
    print(row)

for j in range(1, n):   #Lower part of the Diamond
    dots = ". " * j
    zeros = "0 " * (2 * (n - j) - 1)
    rows = dots + zeros + dots
    print(rows)