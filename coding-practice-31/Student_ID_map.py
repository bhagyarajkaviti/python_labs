#You are given a sequence of student names Ni and their ids Di (corresponding to the student at the same index in Ni). Write a program to print the student name and his ID from Ni and Di in alphabetical order of the name.
#Input
#The first line of input will contain comma-separated strings, denoting the student names (Ni).
#The second line of input will contain comma-separated strings, denoting the corresponding student ids (Di).
#Output
#The output should be M lines equal to the number of students. Each line in the output contains student name and his ID separated by a space in alphabetical order of the name.

names = input().split(",")
ids = input().split(",")



dict_a = {}
for i in range(len(names)):
    dict_a[names[i]] = ids[i]
    
dict_b = sorted(dict_a.items())
for each_tuple in dict_b:
    key, value = each_tuple
    msg = "{} {}"
    print(msg.format(key,value))




#def convert_to_key_value_pairs (keys_list, values_list):
#    dict_a = {}
#    number_of_keys = len (keys_list)
#    for i in range(number_of_keys):
#        key = keys_list[i]
#        value = values_list[i]
#        dict_a[key] = value
#    return dict_a
#student_names = input().split(",")
#student_ids = input().split(",")

#student_details = convert_to_key_value_pairs(student_names, student_ids)
#student_details_items = student_details.items()
#student_details = sorted(student_details_items)
#for item in student_details:
#    print(*item)