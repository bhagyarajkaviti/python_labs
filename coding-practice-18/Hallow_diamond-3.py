# Given an integer N, write a program to print the hollow diamond pattern in 2*N rows and 2*N columns, similar to the pattern shown below.

#   * * * * * * * * * *
#   * * * *     * * * * 
#   * * *         * * *
#   * *             * *
#   *                 *
#   * *             * * 
#   * * *         * * * 
#   * * * *     * * * *   
#   * * * * * * * * * *
n = int(input())


for i in range(n):  # Upper part of the Diamond
  hallow_space = "  " * (i) * 2  
  row = "* " * (n - i) + hallow_space + "* " * (n -i)
  print(row)
  
for j in range(1, n+1): # Lower Part of the Diamond
    hallow_space = "  " * (n-j)*2
    row = "* " * j + hallow_space + "* " * j
    print(row)