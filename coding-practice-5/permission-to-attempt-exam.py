#Given a student's percentage of attendance and status of having a medical report. Write a program to decide if a student is eligible to take the final exam.
#If the student has greater than or equal to 75% of attendance, print "Allowed to write exam".
#If the student has less than 75% of attendance and has a medical reason is equal to "Y", print "Allowed to write exam".
#If the student has attendance less than 75% with no medical reason is equal to "N", print "Cannot write exam".

percentage = input()
percentage = int(percentage[:len(percentage) - 1])

medical_reason = input()


if percentage >= 75 and (medical_reason == "Y" or medical_reason == "N"):
    print("Allowed to write exam")
elif percentage < 75 and medical_reason == "Y":
    print("Allowed to write exam")
elif percentage < 75 or medical_reason == "N":
    print("Cannot write exam")