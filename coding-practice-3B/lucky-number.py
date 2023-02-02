#Write a program that reads two numbers A and B and checks if one of the below conditions is satisfied.
    #One of A and B is equal to 6.
    #The sum of A and B is equal to 6.
    #The difference between A and B is equal to 6.
#Print Lucky if one of the given conditions is satisfied. Otherwise, print Not Lucky.
A = int(input())
B = int(input())

condition1 = A == 6 or B == 6
condition2 = (A + B) == 6
condition3 = (A - B) == 6 or (B - A)== 6

if (condition1 or condition2 or condition3):
    print("Lucky")
else:
    print("Not Lucky")