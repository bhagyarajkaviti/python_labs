#For this problem, the prefilled code will contain a list. Write a program to insert a number (N) at the given index (1) location in the list.
nums_list = [10, 20, 40, 50, 60]
# Write your code here
item = int(input())
index = int(input())
nums_list.insert(index,item)
print(nums_list)