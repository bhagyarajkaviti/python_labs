#Arun is in a class with N students. He has been assigned the responsibility of measuring the height of each student in the class.
#After completing the above-mentioned task, the teacher asked him the Q queries. In each query, he will be given a number X and his task is to find the number of students in the class who have a height of at least X. Help Arun by answering his teacher's queries.
#Write a program that reads N students' heights and Q queries asked by the teacher and prints the answers to each query.
#Input
#The first line of input contains space-separated integers representing number of students N number of queries Q. and
#The second line of input contains N space-separated integers representing the heights of N students in the class.
#The next Q lines of input contain an integer value representing each query X asked by the teacher.

n,q = map(int, input().split())
students_heights = list(map(int, input().split()))
for queries in range(q):
    query = int(input())
    count = 0
    for i in range(len(students_heights)):
        if students_heights[i] >= query:
            count += 1
    print(count)