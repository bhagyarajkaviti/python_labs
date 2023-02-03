#write a program to print the smallest among the given N numbers.
n = int(input())

first_number = int(input())
minimum = first_number
for i in range(n - 1):
    number = int(input())
    if minimum >= number:
        minimum = number
   
print(minimum)