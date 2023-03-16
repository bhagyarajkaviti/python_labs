#Write a program to recursively compute the sum of all the digits in the given number N.
def sum_of_the_digits (number):
    if number < 10: # Base case
        return number
    else:
        a = number % 10  #===> for debugging purpose only
        b = number//10   #===> for debugging purpose only
        return (number % 10) + sum_of_the_digits (number//10) # Recursion
        
number = int(input())
result = sum_of_the_digits (number)
print (result)


#Another solution for the same question

#def sum_of_the_digits(number):
    # Complete this recursive function
#    number = str(number)
#    length = len(number)
#    summ = 0
#    for i in range(length):
#        summ += int(number[i])
    
#    return summ

#number = int(input())
# Call the sum_of_the_digits function
#result =  sum_of_the_digits(number)
#print(result)