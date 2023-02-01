#Write a program that reads an age A and guardian status S, and checks if the age A is between 12 and 60 or if the guardian status S is equal to yes.
# Note: The guardian status will be either yes or no.
age = int(input())
status = input()

age_check = (age >12 and age < 60)
status_check = (status == "yes")

result = age_check or status_check
print(result)