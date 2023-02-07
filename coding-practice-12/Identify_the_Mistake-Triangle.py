#Write a program to print the triangle pattern of a given N number of rows using an asterisk (*) character.
n = int(input())

k = n - 1
for i in range(1, n + 1):
    spaces = " " * k
    stars = "* " * i
    print(spaces+stars)
    k = k - 1
