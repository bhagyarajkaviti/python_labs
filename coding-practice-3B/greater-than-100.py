#Write a program that reads three numbers A, B, and C, and checks if each number is greater than 100.
    #Print All are greater than 100 if each number is greater than 100. Otherwise, print Not all are greater than 100.
A = int(input())
B = int(input())
C = int(input())

if (A > 100 and B > 100 and C > 100):
    print("All are greater than 100")
else:
    print("Not all are greater than 100")