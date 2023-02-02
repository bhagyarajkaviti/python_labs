#Given a number of days (N) as input, write a program to convert N to years (Y), weeks (W), and days (D).
number = int(input())

years = int(number / 365)
reminder1 = number % 365
weeks = int(reminder1 / 7)
reminder2 = reminder1 % 7
days = reminder2

print(str(years) + " years " + str(weeks) + " weeks " + str(days)+" days")