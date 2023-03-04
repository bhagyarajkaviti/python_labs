#Given two Unicode values M and N, write a program to print characters with Unicode values from M to N each on a new line.
m = int(input())
n = int(input())

for i in range(m, n +1):
    char = chr(i)
    print(char)