#Write a program that reads a number N and prints a Right Angled Triangle of N rows using stars ( ) and pluses ( + ).
#The first N-1 rows contains stars (*) and the Nth row contains pluses ( + ).
#*
#* *
#* * * 
#* * * *
#+ + + + +
n = int(input())

for i in range(1, n+1):
    if i < n:
        print("* "* i)
    else:
        print("+ " * i)