#You are given N inputs. Print the given inputs until you encounter a multiple of 5.
n = int(input())

for i in range(1, n + 1):
    number = int(input())
    if number % 5 == 0:
        pass
        break
    else:
        print(number)