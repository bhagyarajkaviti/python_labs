#Write a program that reads the two scores A and B and compares A with the B.
#Print Win if A is greater than B.
#Print Draw if A is equal to B.
#Print Lose if A is less than B.
A = int(input())
B = int(input())

if A > B:
    print("Win")
elif A == B:
    print("Draw")
else:
    print("Lose")