#Write a program that reads a number X and checks,
    #If X is greater than 30.
    #If X is greater than 30, check if X is also greater than 50.
#Print X is greater than 30 if X is greater than 30.
#Print X is greater than 30 and X is greater than 50 on each line if X is greater than 50.
x = int(input())

if x > 30:
    print("X is Greater than 30")
    if x > 50:
        print("X is Greater than 50")