#You are given N numbers as input. Create a list and add the N numbers which are given as input and print the list.
n = int(input())

numbers_list = []
for i in range(n):
    numbers = int(input())
    numbers_list += [numbers]
    
print(numbers_list)