#Write a program that reads two numbers A and B, and checks if all the given conditions are satisfied.
    #A and B are divisible by 3.
    #A or B is divisible by 12.
#Print Pair if all the given conditions are satisfied. Otherwise, print Not a Pair.
A = int(input())
B = int(input())

condition1 = A % 3 == 0 and B % 3 == 0
condition2 = A % 12 == 0 or B % 12 == 0

if condition1 and condition2:
    print("Pair")
else:
    print("Not a Pair")