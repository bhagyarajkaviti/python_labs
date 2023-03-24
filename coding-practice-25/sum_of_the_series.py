#A function is given in the prefilled code that takes two numbers X and N as arguments.
#Write a program that returns the sum of the given series up to N terms using Recursion.
#Series:
    # X, X-2, X-4, X-6, ... N terms
def get_sum_of_series(number, number_of_terms):
    series_sum = 0
    for i in range(number_of_terms):
        series_sum += number - i*2
    return series_sum

number = int(input())
number_of_terms = int(input())

series_sum =get_sum_of_series(number, number_of_terms) # Call the get_sum_of_series function
print(series_sum)

#Using recursion


#def get_sum_of_series (number, number_of_terms):
#    if number_of_terms == 1:
#        return number
#    return number + get_sum_of_series (number - 2, number_of_terms - 1)
#number = int(input())
#number_of_terms = int(input())
#series_sum = get_sum_of_series (number, number_of_terms)
#print(series_sum)