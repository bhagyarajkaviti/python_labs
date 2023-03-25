#For this problem, the prefilled code will contain a list of tuples. Write a program to replace the last number of each tuple in the list with the given number (N).
num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

n = int(input())
output_list = []
for item in num_list:
    updated_item = item[:-1] + (n,)
    output_list.append(updated_item)
    
print(output_list)