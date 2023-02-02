#Write a program that reads the student's marks as input and prints PASS or FAIL.If the student has scored more than 50, print PASS. In all other cases print FAIL.
marks = int(input())

if marks > 50:
    print("PASS")
else:
    print("FAIL")