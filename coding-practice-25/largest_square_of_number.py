#A function is given in the prefilled code that takes a list L as an argument.
#Write a program to find the largest of the squares of the numbers in the list L using Recursion.

#def get_largest_square(numbers):
#    for i in range(len(numbers)):
#        numbers[i] = int(numbers[i])
#        if numbers[i] < 0:
#            numbers[i] = - numbers[i]
#    largest = max(numbers)
#    square = largest ** 2
#    return square
    
#numbers = input().split()

#result =get_largest_square(numbers) # call the get_largest_square function
#print(result)



#Using Recursion

def get_largest_square (numbers): 
    each_number_square = int (numbers[0]) ** 2
    if len(numbers) == 1:
        return each_number_square
    return max(each_number_square, get_largest_square(numbers[1:]))
    
numbers = input().split()

result = get_largest_square(numbers)
print(result)

