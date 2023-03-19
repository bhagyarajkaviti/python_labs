#You are given an integer N as input. Write a program to read N inputs and print a list containing the elements in the last half of the list.
n = int(input())
number_list = input().split()

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
    
length = len(number_list)
half = length//2

if length % 2 == 0:
    print(number_list[half:])
else:
    print(number_list[half+1:])