#For this problem, the prefilled code will contain a list of tuples. Write a program to create a list with the values at the given indexes.
#Input
#The first line of input will contain a positive integer (N).
#The next N lines will contain two space-separated integers. The first number will be the index of the tuple.
#The second number will be the index of the value in the tuple.
#Output
#The output should be a single line containing the list of values in the order of inputs given.
def str_to_int(num_list):
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')] #prefilled code

n = int(input())
output_list = []
for i in range(n):
    num_list = input().split()
    int_list = str_to_int(num_list)
    index_1 = int_list[0]
    index_2 = int_list[1]
    output_list_item = list_a[index_1][index_2]
    output_list.append(output_list_item)
print(output_list)