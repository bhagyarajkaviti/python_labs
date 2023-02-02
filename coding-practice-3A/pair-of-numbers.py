#Write a program that reads two numbers A and B and checks if both A and B are less than or equal to 1000 or B is greater than 500.
    #Print Pair if both A and B are less than or equal to 1000 or B is greater than 500. Otherwise, print Not a Pair.
A = int(input())
B = int(input())

if (A <= 1000 and B <= 1000) or (B > 500):
    print("Pair")
else:
    print("Not a Pair")