#For this problem, the prefilled code will contain a list of tuples. Write a program to print the index of the given number N in the list of tuples.
#Input
#The input will be a single line containing an integer (N).
#Output
#The output should be a single line containing two numbers separated by space.
#The first number should be the index of tuples that contain the number N.
#The second number should be the index of the number N in the tuple.
num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]

n = int(input())
for tuple_item in num_list:
    membership_check = n in tuple_item
    if membership_check:
        list_index = num_list.index(tuple_item)
        tuple_index = tuple_item.index(n)
        print(str(list_index) + " " + str(tuple_index))
        break




#n = int(input())
#output = ""
#for i in range(len(num_list)):
#    for j in range(len(num_list[i])):
#        if num_list[i][j] == n:
#            print(str(i) + " " + str(j))