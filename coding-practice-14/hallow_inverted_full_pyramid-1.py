#Given the number of rows N, write a program to print the hallow inverted full pyramid pattern similar to the pattern shown below.
#   * * * * *
#    *     *
#     *   * 
#      * *
#       *
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print("* " * n)
    elif i == n:
        print(" " * (i - 1) + "* ")
    else:
        left_space = " " * (i - 1)
        hallow_space = "  " * (n - 1 -i)
        print(left_space + "* " + hallow_space + "* ")
        