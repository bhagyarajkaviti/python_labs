#Given the number of rows N, write a program to print the hallow full pyramid pattern similar to the pattern shown below.
#       *
#      * *
#     *   *
#    *     *
#   * * * * *
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print("* "* n)
    else:
        left_space = " " * (n - i)
        hallow_space = "  " * (i - 2)
        print(left_space + "* " + hallow_space + "*")