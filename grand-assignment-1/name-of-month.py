#Given the number of the month, write a program to print the name of the month.
#Input
#The input will be a single line containing a integer N
#Output
#If the given number of the month is 1, print "January".        #If the given number of the month is 2, print "February".
#If the given number of the month is 3, print "March".          #If the given number of the month is 4, print "April".
#If the given number of the month is 5, print "May".            #If the given number of the month is 6, print "June".
#If the given number of the month is 7, print "July".           #If the given number of the month is 8, print "August".
#If the given number of the month is 9, print "September".      #If the given number of the month is 10, print "October".
#If the given number of the month is 11, print "November".      #If the given number of the month is 12, print "December".
#If the given number of the month is less than 1 or greater than 12, print "Invalid Month Number".
month = int(input())

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid Month Number")