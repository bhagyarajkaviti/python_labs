#Given N number of days as input, write a program to convert N number of days to years ( Y ), weeks (W) and days (D).
#Note: Take 1 year = 365 days.
days = int(input())

years = int(days / 365)
print(years)

weeks = int((days % 365) / 7)
print(weeks)

days = (days % 365) % 7
print(days)