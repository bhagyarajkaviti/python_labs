#For this problem, the prefilled code will contain a list. You need to concatenate the given number to the list. 
#The first list should have the number concatenated at the beginning. The second list should have the number concatenated at the end.
num_list =  [10, 20, 40, 100]
n = int(input())
first_list = [n] + num_list# Add the number in the beginning
second_list = num_list + [n]# Add the number at the end

print(first_list)
print(second_list)
