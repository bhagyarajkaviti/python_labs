#Given the number of rows N, write a program to print the inverted full pyramid pattern similar to the pattern shown below.
#   * * * * * 
#    * * * *
#     * * *
#      * * 
#       *
n = int(input())

for i in range(n):
    left_space = " " * (i)
    stars = "* " * (n - i)
    output = left_space + stars
    print(output)
        