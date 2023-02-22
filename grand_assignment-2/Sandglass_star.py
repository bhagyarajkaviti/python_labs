#Given an integer N, write a program to print the sandglass star pattern, similar to the pattern shown below.
n = int(input())

for i in range(n):
    left_space = " " * (i)
    star = "* " * (n - i)
    print(left_space + star)
for j in range(2, n + 1):
    left_space = " " * (n - j)
    star = "* " * j
    print(left_space + star)