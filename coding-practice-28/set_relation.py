#For this problem, the prefilled code will contain a set. Write a program to check the following relations with the given set.
    #1. Superset
    #2. Subset
    #3. Disjoint Set
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

input_num_list = input().split()
for i in range(len(input_num_list)):
    input_num_list[i] = int(input_num_list[i])
input_num_set = set(input_num_list)
if num_set.issubset(input_num_set):
    print("Subset")
elif num_set.issuperset(input_num_set):
    print("Superset")
else:
    print("Disjoint Set")
