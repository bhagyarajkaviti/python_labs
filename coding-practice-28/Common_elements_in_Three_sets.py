#Write a program to find the common elements in the three sets.
#Input:
#The first line of input will contain space-separated integers. 
#The second line of input will contain space-separated integers.
#The third line of input will contain space-separated integers.
#Output:
#The output should be a single line containing the list of common elements in three sets sorted in ascending order.
def str_to_int_list(num_list):
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    num_set = set(num_list)
    return num_set


input_list1 = input().split()
input_list2 = input().split()
input_list3 = input().split()

int_set1 = str_to_int_list(input_list1)
int_set2 = str_to_int_list(input_list2)
int_set3 = str_to_int_list(input_list3)

common_elements = int_set1 & int_set2 & int_set3
print(sorted(common_elements))





#def convert_string_to_int(list_a):  # function to convert string to int
#  new_list = []
#  for item in list_a:
#    num = int(item)
#    new_list.append(num)
#  return new_list

#num_list = []        # list containing three sets whose common lement we need to find 
#for i in range(3):
#  values_list = input().split()
#  values_list = convert_string_to_int(values_list)
#  values_set = set(values_list)
#  num_list.append(values_set)

#intersection_a = num_list[0].intersection(num_list[1])
#intersection_b = intersection_a.intersection(num_list[2])


#result = list(intersection_b)
#result.sort()
#print(result)