#Write a program that reads the rank R of a student and checks,
    #If R is less than or equal to 3.
    #If R is not less than or equal to 3, check if R is less than or equal to 10.
#Print One of Top 3 if the R is less than or equal to 3.
#Print Not Top 3 but One of Top 10 if R is less than or equal to 10 but not less than or equal to 3.
rank = int(input())

if rank <= 3:
    print("One of Top 3")
elif rank <= 10:
    print("Not Top 3 but One of Top 10")