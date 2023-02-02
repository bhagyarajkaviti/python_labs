#Write a program that reads the weight W of a box in kg and checks,
    #If W is greater than or equal to 100.
    #If W is not greater than or equal to 100, check if W is greater than or equal to 30.
#Print Box is Heavier if W is greater than or equal to 100.
#Print Box is Heavy if W is not greater than or equal to 100 but greater than or equal to 30.
weight = int(input())

if weight >= 100:
    print("Box is Heavier")
elif weight >= 30:
    print("Box is Heavy")