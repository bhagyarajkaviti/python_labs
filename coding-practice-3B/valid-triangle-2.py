#Write a program that reads the three angles A, B, and C of a Triangle and checks if the sum of the three angles of the Triangle is equal to 180.
    #Print the Triangle as given below if the sum of the three angles of the Triangle is equal to 180. Otherwise, print Not a Valid Triangle.
A = int(input())
B = int(input())
C = int(input())

if (A + B + C) == 180:
    print("*")
    print("**")
    print("***")
else:
    print("Not a Valid Triangle")