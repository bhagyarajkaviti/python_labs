#Write a program that reads a day number and checks if the day is Week Start, Weekend, or Midweek.
#Day Number                   Day
#    1                      Monday
#    2                      Tuesday         Note: Monday and Tuesday are Week Start.
#    3                      Wednesday             Wednesday, Thursday and Friday are Midweek.
#    4                      Thursday              Saturday and Sunday are Weekend.
#    5                      Friday
#    6                      Saturday
#    7                      Sunday
#For example,
#If the given day number is 1, the day name is Monday,
#If the given day number is 2, the day name is Tuesday, etc.
n = int(input())

if n <= 2:
    print("Week Start")
elif 2 < n <= 5:
    print("Midweek")
elif 5 < n <= 7:
    print("Weekend")