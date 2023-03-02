#Write a program to print a list with the given N inputs.
n = int(input())

list_1 = []
for i in range(n):
    items = input()
    list_1 += [items]
print(list_1)