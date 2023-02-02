#Write a program that reads the rank of a student R and checks if R is less than 10.
#Print HONOR STUDENT if R is less than 10. Otherwise, print NORMAL STUDENT.
rank = int(input())

if rank < 10:
    print("HONOR STUDENT")
else:
    print("NORMAL STUDENT")