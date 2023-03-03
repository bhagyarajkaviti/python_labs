#Given seconds as input, write a program to print in D days H hours M minutes S seconds.
n = int(input())

days = int(n/86400)
days_remainder = n % 86400 

hours = int(days_remainder/3600)
hours_remainder = days_remainder % 3600

minutes = int(hours_remainder/60)
minutes_remainder = hours_remainder % 60

seconds = minutes_remainder
if n >= 86400:
    if n % 86400 == 0:
        print(str(days) + " " + "Days")
    elif days_remainder % 3600 == 0:    
        print(str(days) + " " + "Days" + " " + str(hours) + " " + "Hours")
    elif hours_remainder % 60 == 0:
        print(str(days) + " " + "Days" + " " + str(hours) + " " + "Hours" + " " + str(minutes) + " " + "Minutes")
    elif minutes_remainder != 0:
        print(str(days) + " " + "Days" + " " + str(hours) + " " + "Hours" + " " + str(minutes) + " " + "Minutes" + " " + str(seconds) + " " + "Seconds")
elif 86400 > n >= 3600:
    if n % 3600 == 0:
        print(str(hours) + " " + "Hours")
    elif hours_remainder % 60 == 0:
        print(str(hours) + " " + "Hours" + " " + str(minutes) + " " + "Minutes")
    elif minutes_remainder != 0:
        print(str(hours) + " " + "Hours" + " " + str(minutes) + " " + "Minutes" + " " + str(seconds) + " " + "Seconds")
elif 3600 > n >= 60:
    if n % 60 == 0:
        print(str(minutes) + " " + "Minutes")
    elif minutes_remainder != 0:
        print(str(minutes) + " " + "Minutes" + " " + str(seconds) + " " + "Seconds")
elif n < 60:
    print(str(seconds) + " " + "Seconds")