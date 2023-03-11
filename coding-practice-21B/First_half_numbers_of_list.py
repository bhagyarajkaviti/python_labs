#Given space-separated numbers, write a program that creates a list using space-separated numbers and prints the first half of the numbers of the list as a new list.
#Note
#If the given number of words is an odd number, add one to it such that it becomes an even number and count half of the number of words.
number_list = input().split()

len_of_list = len(number_list)
half_length = int(len_of_list/2)
output_list = []
for i in number_list:
    output_list += [int(i)]

if len_of_list % 2 == 0:
    print(output_list[:half_length])
else:
    print(output_list[:half_length + 1])


#HERE IS THE ANOTHER SOLUTION:

#number = input()
#number_split = number.split()
#length = len(number_split)

#if length % 2 == 0:
#    length = length // 2
#    result = number_split[:length]
#else:
#    length = length // 2 + 1
#    result = number_split[:length]

#for i in range (len(result)):
#    result[i] = int(result[i])
#    
#print(result)
    