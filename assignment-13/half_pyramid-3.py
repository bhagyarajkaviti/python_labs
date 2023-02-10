#Given an integer N as a starting number and K as input, write a program to print a number pyramid of K rows as shown below.
stat_num = int(input())
rows = int(input())

number = stat_num
for i in range(1, rows+1):
    output = ""
    for j in range(i):
        output = output + str(number) + " "
        number = number + 1    
    print(output)