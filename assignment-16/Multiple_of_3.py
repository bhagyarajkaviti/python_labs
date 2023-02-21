#You are given N inputs. Print the numbers that are multiples of 3.
n = int(input())

for i in range(1, n+1):
    number = int(input())
    if number % 3 == 0:
        print(number)