#You are given two integers M, N as input. Write a program to print all the composite numbers present in the given range (including M and N ).
#NOTE: Composite numbers are those numbers that have more than two factors. In other words, composite numbers have factors other than 1 and itself.
m = int(input())
n = int(input())

for i in range(m , n + 1):
    factor = 0
    for j in range(1, i + 1):
        if i % j == 0:
            factor = factor + 1
        if factor > 2:
            print(i)
            break
    