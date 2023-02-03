#Write a program to print a hollow square pattern of N rows and N columns using the asterisk character (*), where integer N is given as an input.
n = int(input())

for i in range(1 , n+1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "*")