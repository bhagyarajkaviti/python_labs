#A function is given in the prefilled code that takes a list L as an argument.
#Write a program that returns the sum of the squares of the numbers in the list L using Recursion.
def get_sum_of_squares(numbers):
    sum_of_squares = 0
    for i in numbers:
        sum_of_squares += int(i) ** 2
    return sum_of_squares
    
numbers = input().split()

squares_sum = get_sum_of_squares(numbers)# Call the get_sum_of_squares function
print(squares_sum)

#Using Recursion

#def get_sum_of_squares (numbers): 
#    each_number = int(numbers[0])
#    if len(numbers) == 1: 
#        return each_number ** 2
#    return each_number ** 2 + get_sum_of_squares(numbers [1:])
#numbers = input().split()
#squares_sum = get_sum_of_squares (numbers)
#print(squares_sum)