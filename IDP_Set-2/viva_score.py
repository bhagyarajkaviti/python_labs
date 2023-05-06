#The N students in the class have recently finished a science viva exam and received their results from the teacher. They are standing in the order in which they took the exam, each holding their results in hand.
#The teacher asked the students to note the number of students who took the viva after them and received a lower score. Your task is to help students.
#Write a program that reads N space-separated viva scores of students and prints the number of students who took the viva after them and received a lower score.
#Input
#The first line of input contains an integer representing the number of students N.
#The second line of input contains N space-separated integers representing the viva scores of students S.

n = int(input())
scores = list(map(int,input().split()))

output = []
for i in range(len(scores)):
    right_slice = scores[i+1:]
    count = 0
    for j in right_slice:
        if scores[i] > j:
            count += 1
    output.append(count)
print(*output)