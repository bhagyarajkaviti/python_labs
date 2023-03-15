#Write a program to print the Kth smallest number in the list.
number_list = input().split(",")
k = int(input())

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
    
sorted_list = sorted(number_list)
#print(sorted_list)
kth_smallest_number = sorted_list[k-1]
print(kth_smallest_number)