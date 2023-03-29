#Write a program to remove the elements other than numbers in the list.
def str_to_int_list(input_list):
    output_list = []
    for i in input_list:
        if i.isdigit():
            output_list += [int(i)]
        else:
            pass
    return output_list
 
input_list = input().split(",")
print(str_to_int_list(input_list))