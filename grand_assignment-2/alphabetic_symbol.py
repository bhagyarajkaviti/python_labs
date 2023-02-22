#Write a program to print the right alphabetic triangle up to the given N rows.
#   A
#   A B
#   A B C
#   A B C D
n = int(input())
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(alphabets)

output = ""
for row in range(n):
    output = output + alphabets[row] + " "
    print(output)