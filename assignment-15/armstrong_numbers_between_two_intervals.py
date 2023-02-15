#Write a program to print all the Armstrong numbers in the given range A to B (including A and B). An N-digit number is an Armstrong number if the number equals the sum of the Nth power of its digits.
a = int(input())
b = int(input())


output = ""
Armstrong = False
for i in range(a , b+1):
    number = str(i)
    length = len(number)
    sum = 0
    for j in number:
        sum = sum + int(j) ** length
    if (sum) == (i):
        output = output + str(sum) + " "
        Armstrong = True
if Armstrong:
    print(output)
else:
    print("-1")