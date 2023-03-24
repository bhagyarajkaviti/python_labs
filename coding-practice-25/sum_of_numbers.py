#A function is given in the prefilled code that takes a list L as an argument.
#Write a program that returns the sum of the numbers in the list L using Recursion.

def get_sum (numbers): 
    each_number = int(numbers[0])
    if len(numbers) == 1:
        return each_number
    return each_number + get_sum(numbers [1:])
    
numbers = input().split()

sum_of_numbers = get_sum(numbers) 
print(sum_of_numbers)


#Using Recursion

#def get_sum(numbers):
#    sum_of_num = 0
#    for i in numbers:
#        sum_of_num += int(i)
#    return sum_of_num

#numbers = input().split()

#sum_of_numbers =get_sum(numbers) # Call the get_sum function
#print(sum_of_numbers)