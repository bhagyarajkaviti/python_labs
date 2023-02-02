#Given two integers A and B, write a program to print the relation between the two numbers.
#If A is equal to B, print "A == B".
#If A is greater than B, print "A > B".
#If A is less than B, print "A < B".
A = int(input())
B = int(input())

if A == B:
    print("A == B")
elif A > B:
    print("A > B")
elif A < B:
    print("A < B")