#Write a program that reads three numbers A , B, C and prints the greatest among the three numbers.
A = int(input())
B = int(input())
C = int(input())

condition1 = A >= B and A >= C
condition2 = B > C and B > A
condition3 = C > A and C > B
 
if condition1:
    print(A)
if condition2:
    print(B)
if condition3:
    print(C)

#a = int(input())
#b = int(input())
#c = int(input()) 

#if a > b:
    #greatest_number = a
#else:
    #greatest_number = b
#if c > greatest_number:
    #greatest_number = c
    
#print(greatest_number)