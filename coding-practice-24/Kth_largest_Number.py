#Write a program to print the Kth largest number in the list.
number_list = input().split(",")
k = int(input())

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
    
sorted_list = sorted(number_list)
#print(reverse_sorted_list)
kth_largest_number = sorted_list[-k]
print(kth_largest_number)