#Given a time T in either Minutes (M) or Seconds ( S ).
#Example: 220M, 3S.
#If the last character in the T is M, it is Minutes.
#If the last character in the T is S, it is Seconds.
#Write a program to convert the given time T in Minutes (M) or Seconds (S) into Hours (H) rounded up to 2 decimals.
#The last character of the output should be H representing time in Hours.
time = input()
number = int(time[:len(time) - 1])

if time[len(time) - 1] == "M":
    hours = number/60
    print(str(round(hours,2)) + "H")
elif time[len(time) - 1] == "S":
    hours = number / 3600
    print(str(round(hours,2)) + "H")
else:
    print("enter correct input format")