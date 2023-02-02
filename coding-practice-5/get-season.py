#Write a program to find season for the given month number.
#If the given month is either November or December or January, print "Winter".
#If the given month is either February or March, print "Spring".
#If the given month is either April or May or June print "Summer".
#If the given month is either July or August, print "Rainy".
#If the given month is either September or October, print "Autumn".
month = int(input())
if month == 11 or month == 12 or month == 1:
    print("Winter")
elif month == 2 or month == 3:
    print("Spring")
elif month == 4 or month == 5 or month == 6:
    print("Summer")
elif month == 7 or month == 8:
    print("Rainy")
elif month == 9 or month ==10:
    print("Autumn")