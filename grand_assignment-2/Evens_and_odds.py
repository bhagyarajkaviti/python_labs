#Write a program to count even and odd numbers in given range [M, N]. Both M, N are inclusive in [M, N].
m = int(input())
n = int(input())

even = 0
odd = 0

for i in range(m , n+1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(odd)
print(even)