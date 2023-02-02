#Write a program to print a greeting message based on the given time.
#If the time is greater than or equal to 4 and less than 12, print "Good Morning".
#If the time is greater than or equal to 12 and less than 16, print "Good Afternoon".
#If the time is greater than or equal to 16 and less than 20, print "Good Evening".
#If the time is greater than or equal to 20 or less than 4, print "Good Night".
time = int(input())

if 4 <= time < 12:
    print("Good Morning")
elif 12 <= time < 16:
    print("Good Afternoon")
elif 16 <= time < 20:
    print("Good Evening")
else:
    print("Good Night")