#You are given N as input. Write a program to print the pattern of 2*N-1 rows using an asterisk (*) as shown below.
#Note: There is a space after each asterisk character.
#   * * * *
#   *     *
#   *     *
#   * * * *
#         *
#         *
#   * * * *   
n = int(input())

for i in range(1, 2*n):
    if i == 1 or i == n or i == 2 *n - 1:
        print("* " * n)
    elif i < n:
        print("* " + "  " * (n - 2) + "* ")
    else:
        print("  " * (n-1) + "* ")