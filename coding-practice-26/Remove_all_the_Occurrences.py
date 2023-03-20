#For this problem, the prefilled code will contain a list. Write a program to remove all the occurrences of the given number (N) in a list.
nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# Write your code here
n = int(input())
count = nums_list.count(n)
for i in range(count):
    nums_list.remove(n)

print(nums_list)