#For this problem, the prefilled code will contain an MXN matrix. Write a program to print the row and column containing the maximum element.
#Input
#The first line of input will contain two space-separated integers, denoting the M and N.
#The next M following lines will contain N space-separated integers, denoting the elements of each list.
#Output
#The first line of output should be a list containing the row elements which has the maximum element.
#The second line of output should be a list containing the column elements which has the maximum element.

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)
#print(num_list)

# Write your code here
all_elements_list = []
for list_item in num_list:  # converting nested list items into single list items .
    all_elements_list.extend(list_item)
maximum_element = max(all_elements_list)

for list_item in num_list:  #printing the first line of the output. printing row elements which has maximum element.
    if maximum_element in list_item:  # Membership check
        index = list_item.index(maximum_element) # To find index of the maximum element in the row(list_item)
        print(list_item)
        break
second_line_output = []
for list_item in num_list:  # Printing the second line of the output. i.e, column elements which has the maximum element.
    second_line_output.append(list_item[index])
print(second_line_output)