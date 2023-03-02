#You are given an integer N as input. Write a program to read N integers and print a list containing the first and last two inputs.
n = int(input())

full_list = []
for i in range(n):
    numbers = int(input())
    full_list += [numbers]
    
new_list = full_list[:2] + full_list[(n - 2):]
print(new_list)