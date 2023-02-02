#Write a program that reads the age of a person and checks if the age of the person is greater than or equal to 18 for eligibility to vote.
    #Print Eligible if the age of the person is greater than or equal to 18, otherwise print Not Eligible.
age = int(input())

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")