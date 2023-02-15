#Given an integer N, write a program to print the solid half diamond pattern in (2*N - 1) rows and N columns, similar to the pattern shown below
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * * 
#   * * * 
#   * * 
#   *
n = int(input())

for i in range(1, n + 1):
    print("* " * i)
    
for j in range(1, n):
    print("* " * (n - j))