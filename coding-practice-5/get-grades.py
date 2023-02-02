#Write a program to calculate the grade of the student based on marks he/she scored.
#If the given marks are greater than 85, print "A".
#If the given marks are greater than 70 and less than or equal to 85, print "B".
#If the given marks are greater than or equal to 60 and less than or equal to 70, print "C".
#If the given marks are less than 60, print "F".
marks = float(input(""))

if marks > 85:
    print("A")
elif 70 < marks <= 85:
    print("B")
elif 60 < marks <= 70:
    print("C")
else:
    print("F")
