#Write a program that reads the size S and page ount C of a book and checks if S is equal to large or C is greater than or equal to 300.
    #print Buy a Book if S is equal to large or C is greater than or equal to 300. Otherwise, print Do Not Buy a Book.
size = input()
count = int(input())

if (size == "large" or count >= 300):
    print("Buy a Book")
else:
    print("Do Not Buy a Book")