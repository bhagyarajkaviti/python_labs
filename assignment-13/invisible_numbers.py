#You are given a positive integer N. Your task is to find the number of positive integers K <= N such that K is not divisible by any of the following numbers 2, 3, 4, 5, 6, 7, 8, 9, 10.
n=int(input())
count=0


for i in range(1,n+1):
    is_divisible="True" 
    for j in range(2,11):
        if (i%j==0): 
            is_divisible="False"
           
    if is_divisible == "True": # Added condtional block for increasing count
        count = count + 1
print(count) 