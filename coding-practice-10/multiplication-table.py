#Write a program to print the multiplication table of the given number (N) up to ten multiples in the format "Nx i = M".
n = int(input())

for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(n*i))
