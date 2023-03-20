#Consider a list (nums_list = []). Write a program to perform the following commands on the list
#1. insert | E - insert the integer E at index I
#2. append E - insert integer E at the end of the list
#3. pop remove the last element
#4. remove E - remove the first occurrence of integer E
#5. sort - sort the list in ascending order
#6. print print the list
n = int(input())

nums_list = []

for i in range(n):
    command = input().split()

    if command[0] == 'insert':
        index = int(command[1])
        value = int(command[2])
        nums_list.insert(index, value)
    elif command[0] == 'append':
        value = int(command[1])
        nums_list.append(value)
    elif command[0] == 'pop':
        nums_list.pop()
    elif command[0] == "remove":
        value = int(command[1])
        nums_list.remove(value)
    elif command[0] == "sort":
        nums_list.sort()
    elif command[0] == "print":
        print(nums_list)
