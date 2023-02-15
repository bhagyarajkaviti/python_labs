#Given the number of rows N, write a program to print the pyramid pattern similar to the pattern shown below.
#   0 0 0 0 1 0 0 0 0
#   0 0 0 1 1 1 0 0 0
#   0 0 1 1 1 1 1 0 0
#   0 1 1 1 1 1 1 1 0
#   1 1 1 1 1 1 1 1 1 
n = int(input())

for i in range(1, n + 1):
    zeros = "0 " * (n -i)
    middle_pyramid = "1 " * (2 * i - 1)
    print(zeros + middle_pyramid + zeros)