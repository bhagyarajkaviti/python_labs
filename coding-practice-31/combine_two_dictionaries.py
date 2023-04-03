#Write a program to combine two dictionaries updating values for common keys.
#Input
#The first line of input will contain space-separated strings, denoting the keys of first dictionary.
#The second line of input will contain space-separated integers, denoting the values of first dictionary.
#The third line of input will contain space-separated strings, denoting the keys of second dictionary.
#The fourth line of input will contain space-separated integers, denoting the values of second dictionary.
#Output
#The output should be a single line containing the list of tuples of dictionary items with all the key-value pairs of two dictionaries sorted in ascending order by key.

def convert_to_key_value_pairs(keys_row, values_row):
    dict_a = {}
    for i in range(len(keys_row)):
        dict_a[keys_row[i]] = int(values_row[i])
        
    return dict_a
        
    
keys_row_1 = input().split()
values_row_1 = input().split()
keys_row_2 = input().split()
values_row_2 = input().split()

dict_1 = convert_to_key_value_pairs(keys_row_1, values_row_1)
dict_2 = convert_to_key_value_pairs(keys_row_2, values_row_2)

dict_1.update(dict_2)

output_list = sorted(dict_1.items())
print(output_list)