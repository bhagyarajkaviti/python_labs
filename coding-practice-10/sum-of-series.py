#Write a program to find the sum of the series 2 +22 + 222 + 2222 + . N terms.
n = int(input())

sum = 0
for i in range(1, n+1):
    n = "2" * i
    number = int(n)
    sum += number
print(sum)