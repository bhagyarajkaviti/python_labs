#You are given two numbers, A and B where 1 <= A <= B, Write a program to find the number of perfect squares in the range A to B (including A and B).
a = int(input())
b =int(input())

start = int(a ** 0.5)
if a % (start * start) == 0:
    left = start
else:
    left = start + 1
end = int(b ** 0.5)
if b % (end * end) == 0:
    right = end
else:
    right = end

result = right - left + 1

print(result)

#a=int(input())
#b=int(input())

#c=0
#for i in range(a,b+1):
#    if(i**0.5==int(i**0.5)):
#        c=c+1

#print(c)

    