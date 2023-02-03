#write a program to print the greatest among the given N numbers.
n = int(input())

first_input=int(input())
greatest_number=first_input

for i in range(n-1):
    number=int(input())
    if number>greatest_number:
        greatest_number=number
print(greatest_number)

#n=int(input())
#max = 0
#for i in range (n):
#    num = int(input())
#    if max <= num:
#        max=num
#print(max)
    