#Write a program to print the smallest number in the list.
number_list = input().split(",")

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
    
smallest_number = min(number_list)
print(smallest_number)