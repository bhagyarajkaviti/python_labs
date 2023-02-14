#Given the number of rows N, write a program to print the hallow half pyramid pattern similar to the pattern shown below.
#   *
#   * *
#   *   *  
#   *     *
#   * * * * *
n = int(input())

for i in range(n):
    if i == 0:
        print("* ")
    elif i == n - 1:
        print("* " * n)
    else:
        print("* " + "  " * (i - 1) + "* ")