#Given the number of rows N, write a program to print the hallow inverted half pyramid pattern similar to the pattern shown below.
#   *  *  *  *  *  
#   *        * 
#   *     *         
#   *  *
#   *
n = int(input())

for i in range(n):
    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print("* ")
    else:
        print("* " + "  " * (n - 2 -i) + "* ")