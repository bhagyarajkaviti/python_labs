#Given an integer N as a starting number and K as input, write a program to print a number pyramid of K rows as shown below.
stat_num = int(input())
rows = int(input())

count = 0
for a in range(1, rows + 1):
    count = count + a
number = stat_num + (count - 1)
#step = int((rows * (rows + 1) / 2) - 1)
#number = stat_num + step

for i in range(1, rows+1):
    output = ""
    for j in range(i):
        output = output + str(number) + " " 
        number = number - 1    
    print(output)