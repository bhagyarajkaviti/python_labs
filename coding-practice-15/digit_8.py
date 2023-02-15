#Given an integer N, write a program to print pattern "8" in (2*N + 1) rows and N columns, similar to the pattern shown below
#   * * * * *
#   *       *
#   *       *
#   *       *
#   *       *
#   * * * * *
#   *       *
#   *       *
#   *       *
#   *       *
#   * * * * *
n = int(input())

for i in range(2 * n + 1):
    if i == 0 or i == n or i == 2 * n:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "* ")