#Given comma seperated numbers and an integer K write a program to find all the unique pairs with sum K.
    #Input:5, 3, 7, 9, 5                Output:(3, 9)
    #      12                                  (5, 7)
def convert_str_to_int(str_num_list):
    new_list = []
    for item in str_num_list:
        num_int = int(item)
        new_list.append(num_int)
    return new_list

def get_unique_pairs(int_list,pair_sum):
    stop_index = len(int_list) - 1
    unique_pairs_set = set()
    for cur_index in range(stop_index):
        num_1 = int_list[cur_index]
        num_2 = pair_sum - num_1
        remaining_list = int_list[cur_index+1:] 
        if num_2 in remaining_list:
            pair = (num_1, num_2)
            pair = tuple(sorted(pair))
            unique_pairs_set.add(pair)
    return unique_pairs_set
    



str_num_list = input().split(",")
pair_sum = int(input())

int_list = convert_str_to_int(str_num_list)

unique_pairs = get_unique_pairs(int_list, pair_sum)

for pair in unique_pairs:
    print(pair)