#Given an integer N, write a program to print a pyramid of N rows as shown below.
#   . . . . 0 . . . .
#   . . . 0 0 0 . . .
#   . . 0 0 0 0 0 . .
#   . 0 0 0 0 0 0 0 .
#   0 0 0 0 0 0 0 0 0
n = int(input())

for i in range(1, n + 1):
    dots = ". " * (n - i)
    zeros =  "0 " * (2 * i - 1)
    print(dots + zeros + dots)