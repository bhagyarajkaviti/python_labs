#Write a program that reads a number N and finds the,
    # Remainder when N is divided by 4.
    #Remainder when N is divided by 5.
#Print the greatest remainder among the two remainders when N is divided by 4 and 5.
number = int(input())

remainder_by_4 = number % 4
remainder_by_5 = number % 5

if remainder_by_5 > remainder_by_4:
    print(remainder_by_5)
else:
    print(remainder_by_4)