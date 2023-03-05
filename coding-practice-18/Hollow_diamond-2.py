#Given the number of rows N, write a program to print the hallow diamond pattern similar to the pattern shown below.
#       A   
#      B B
#     C   C
#    D     D
#   E       E
#    D     D
#     C   C
#      B B
#       A
n = int(input())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = alphabet[:n]

for i in range(n):  #Upper part upto n rows
    left_space = (n - i -1) * " "
    letter = alphabet[i]
    if i == 0:  # boundary condition for upper part upto n rows
        print(left_space + letter)
    else:
        hallow_space = " " * (2 * i - 1)
        row = left_space + letter + hallow_space + letter
        print(row)
        
for j in range(1, n):   #lower part remaining (n-1) rows
    left_space = " " * j
    letter = alphabet[n - 1 - j]
    if j == n - 1:
        print(left_space + letter)
    else:
        hallow_space = " " * ((n - j - 1)* 2 - 1)
        print(left_space + letter + hallow_space + letter)