#Given the weekday of the first day of the month, determine the day of the week of the given date in that month.
#Input:
    #The first line is a string D. The second line is an integer N.
#Output:
    #The output should be a string.
day1 = input()
date = int(input())

remainder = date % 7

if day1 == "Monday":
    if remainder == 1:
        print("Monday")
    elif remainder == 2:
        print("Tuesday")
    elif remainder == 3:
        print("Wednesday")
    elif remainder == 4:
        print("Thursday")
    elif remainder == 5:
        print("Friday")
    elif remainder == 6:
        print("Saturday")
    elif remainder == 0:
        print("Sunday")
elif day1 == "Tuesday":
    if remainder == 0:
        print("Monday")
    elif remainder == 1:
        print("Tuesday")
    elif remainder == 2:
        print("Wednesday")
    elif remainder == 3:
        print("Thursday")
    elif remainder == 4:
        print("Friday")
    elif remainder == 5:
        print("Saturday")
    elif remainder == 6:
        print("Sunday")
elif day1 == "Wednesday":
    if remainder == 6:
        print("Monday")
    elif remainder == 0:
        print("Tuesday")
    elif remainder == 1:
        print("Wednesday")
    elif remainder == 2:
        print("Thursday")
    elif remainder == 3:
        print("Friday")
    elif remainder == 4:
        print("Saturday")
    elif remainder == 5:
        print("Sunday")
elif day1 == "Thursday":
    if remainder == 5:
        print("Monday")
    elif remainder == 6:
        print("Tuesday")
    elif remainder == 0:
        print("Wednesday")
    elif remainder == 1:
        print("Thursday")
    elif remainder == 2:
        print("Friday")
    elif remainder == 3:
        print("Saturday")
    elif remainder == 4:
        print("Sunday")
elif day1 == "Friday":
    if remainder == 4:
        print("Monday")
    elif remainder == 5:
        print("Tuesday")
    elif remainder == 6:
        print("Wednesday")
    elif remainder == 0:
        print("Thursday")
    elif remainder == 1:
        print("Friday")
    elif remainder == 2:
        print("Saturday")
    elif remainder == 3:
        print("Sunday")
elif day1 == "Saturday":
    if remainder == 3:
        print("Monday")
    elif remainder == 4:
        print("Tuesday")
    elif remainder == 5:
        print("Wednesday")
    elif remainder == 6:
        print("Thursday")
    elif remainder == 0:
        print("Friday")
    elif remainder == 1:
        print("Saturday")
    elif remainder == 2:
        print("Sunday")
elif day1 == "Sunday":
    if remainder == 2:
        print("Monday")
    elif remainder == 3:
        print("Tuesday")
    elif remainder == 4:
        print("Wednesday")
    elif remainder == 5:
        print("Thursday")
    elif remainder == 6:
        print("Friday")
    elif remainder == 0:
        print("Saturday")
    elif remainder == 1:
        print("Sunday")
