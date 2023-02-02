#Write a program that reads two strings H and I and checks,
    #If H is equal to "Y".
    #If H is not equal to "Y", check if I is equal to "Y".
#Print Allowed to Exam - Has Hall ticket if H is equal to "Y".
#Print Allowed to Exam - Has Identification Card if H is not equal to "Y" and I is equal to "Y".
H = input()
I = input()

if H == "Y":
    print("Allowed to Exam - Has Hall ticket")
elif I == "Y":
    print("Allowed to Exam - Has Identification Card")