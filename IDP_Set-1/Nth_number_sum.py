#Write a program that reads the numbers N, M space-separated numbers and prints the sum of numbers whose position is divisible by N. Consider that the positions of the numbers starts from 1 to M.
#Input
#The first line of input contains the space-separated integers representing N and M.
#The second line of input contains M space-separated integers representing the numbers.
#Output
#The output should be a single line containing an integer that is the sum of all the numbers whose position is divisible by N.

n,m = map(int, input().split())
num_list = list(map(int, input().split()))

addition = 0
for i in range(1,len(num_list)+1):
    if i % n == 0:
        addition += num_list[i-1]
    
print(addition)