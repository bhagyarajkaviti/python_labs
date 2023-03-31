#For this problem, the prefilled code will contain a list of tuples. Write a program to remove the given number N in all the tuples if it present.
#Input
#The input will be a single line containing an integer (N).
#Output
#The output should be a single line containing the list of tuples without the N.

num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)] # Prefilled code

n=int(input())
for i in range(len(num_list)):
    num_list[i]=list(num_list[i])
    if n in num_list[i]:
        num_list[i].remove(n)
    num_list[i]=tuple(num_list[i])
print(num_list)



#n = int(input())

#updated_list = []
#for list_item in num_list:
#    set_ = set(list_item)
#    set_.discard(n)
#    list_ = sorted(list(set_))
#    tuple_ = tuple(list_)
#    updated_list.append(tuple_)
#print(updated_list)