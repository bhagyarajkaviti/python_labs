#Given an integer N, write a program to print the butterfly pattern in 2*N rows and 2*N columns, similar to the pattern shown below
#   *                 *
#   * *             * *
#   * * *         * * *
#   * * * *     * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * *     * * * *  
#   * * *         * * *
#   * *             * *
#   *                 *
n = int(input())

for i in range(1, n + 2):
    if i == n or i == n + 1:
        print("* " * (2 * n))
    else:
        hallow_space = "  " * (n - i) * 2
        print("* " * i + hallow_space + "* " * i)
for j in range(1, n):
    hallow_space = "  " * j * 2
    print("* " * (n - j) + hallow_space + "* " * (n - j))
    