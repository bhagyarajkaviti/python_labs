#Write a program to print the maximum and minimum of all the values at index zero and index one in the list of tuples.
#Input
#The first line of input will contain a positive integer (N).
#The next N lines will contain space-separated two integers, denoting elements of each tuple.
#Output
#The first line of output should contain a tuple with the maximum and minimum value at index zero. The second line of output should contain a tuple with the maximum and minimum value at index one.
def str_to_int(num_list):
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list
    
n = int(input())
index_0_list = []
index_1_list = []
for i in range(n):
    num_list = input().split()
    num_1 = int(num_list[0])
    num_2 = int(num_list[1])
    index_0_list.append(num_1)
    index_1_list.append(num_2)

tuple_1 = (max(index_0_list), min(index_0_list))
print(tuple_1)
tuple_2 = (max(index_1_list), min(index_1_list))
print(tuple_2)
    