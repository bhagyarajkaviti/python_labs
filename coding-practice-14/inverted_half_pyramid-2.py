#Given the number of rows N, write a program to print the inverted half pyramid pattern similar to the pattern shown below.
# * * * * * 
# * * * *
# * * *
# * *
# *
n = int(input())

for j in range(n):
    output = "* " * (n - j)
    print(output)