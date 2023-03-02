#Write a program to read N inputs and print a list containing the first and last three inputs.
n = int(input())

list_1 = []
for i in range(1, n+1):
    item = input()
    if i <= 3 or i > (n - 3):
        list_1 += [item]
        
print(list_1)