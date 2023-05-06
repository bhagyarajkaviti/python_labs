#Professor Michael gave an assignment to his students. The professor divided the students into N groups after they completed the assignment and he would like to know which group achieved the highest score.
#You will be given N groups' assignment scores and your task is to help Professor to know which group of students achieved the highest score on their assignments.
#Write a program that reads the N group of comma-separated assignment scores and prints the group that achieved the highest score.
#Input
#The first line of input contains an integer representing the number of groups N.
#The next N lines of input contain comma-separated integers representing the N group of students assignment scores.

n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split(",")))
    matrix.append(row)
    
sum_matrix = []
for i in matrix:
    sum_matrix.append(sum(i))
index = sum_matrix.index(max(sum_matrix))
print(*matrix[index])