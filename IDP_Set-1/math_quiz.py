#Riya participated in a math quiz competition. At the end of the contest, she had to solve a tricky question to win the first prize.
#She has been given a few numbers, M multiple ranges and her task is to add all the numbers in each corresponding range. Help Riya to solve this question.
#Write a program that reads the space-separated numbers and M multiple ranges and prints the sum of all the numbers in each range.
#Input
#The first line of input contains space-separated integers representing numbers.
#The second line of input contains an integer representing the multiple ranges M.
#The next M lines of input contain space-separated integers representing the each range.


num_list = list(map(int, input().split()))
rows = int(input())
for i in range(rows):
    s,e = map(int, input().split())
    addition = 0
    for num in range(s,e+1):
        if num in num_list:
            addition += num * (num_list.count(num))
    print(addition)