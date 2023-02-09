#Python Program to Print the Fibonacci sequence
nterms = int(input("enter how many terms you want \n"))

n1 = 0
n2 = 1
if nterms <= 0:
    print("enter positive integer")
elif nterms == 1:
    print("The Fibonacci sequence of the numbers upto", nterms, ":")
    print(n1)
else:
    print("The fibonacci sequence of the numbers upto", nterms, ":")
    for i in range(nterms):
        print(n1)
        result  = n1 + n2
        n1 = n2
        n2 = result
