#Write a program to determine whether the given year Y is a leap year or not.
#A normal year consists of 365 days. But the time required for Earth to revolve around the Sun is around 365.2425 days. So a "leap year" of 366 days is used once every four years to eliminate the error caused by three normal (but short) years. Any year that is divisible by 4 is usually a leap year: for example, 1988, 1992, and 1996 are leap years.
#However, there is still a small error that must be accounted for. To eliminate this error, the calendar considers that a year that is divisible by 100 (for example, 1900) is a leap year only if it is also divisible by 400. For this reason, the following years are not leap years: 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600,... This is because they are divisible by 100 but not by 400.
#The following years are leap years: 1600, 2000, 2400 This is because they are divisible by both 100 and 400.
year = int(input())

if year % 400 != 0 and year % 100 == 0:
    print("False")
elif year % 4 == 0:
    print("True")
else:
    print("False")