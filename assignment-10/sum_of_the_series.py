#Write a program to find the sum S of the series where S = x - x^3 + x^5 + ..... upto N terms.
x = int(input())
n = int(input())

positive = 0
j = 1
negative = 0
k = 3
r = int(n / 2)
if n % 2 != 0:
    for i in range(r+1):
        positive += x ** j
        j += 4
    for l in range(r):
        negative += x ** k
        k += 4
elif n % 2 == 0:
    for i in range(r):
        positive += x ** j
        j += 4
    for l in range(r):
        negative += x ** k
        k += 4
        
print(positive - negative)

#another solution for the same question


#A = int(input())
#B = int(input())

#result = 0
#power = 1
#for i in range(0,B):
#    if i % 2==0:
#        result = result + (A ** power)
#       power = power + 2
#    else:
#        result = result - (A ** power)
#        power = power + 2

#print(result)