#A function is given in the prefilled code that takes a number N as an argument.
#Write a program that checks if N is between 200 and 500.
#Print Yes if N is between 200 and 500. Otherwise, print No.
def is_between_200_and_500(number):
    if number >200 and number < 500:
        print("Yes")
    else:
        print("No")
    #complete this function
    

number = int(input())
is_between_200_and_500(number)
#call the is_between_200_and_500 function