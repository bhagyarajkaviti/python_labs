#Write a program that reads the number N and prints the product of its digits.
#Input
#The input will be a single line containing an integer representing the number N.
#Output
#The output should be a single line containing an integer obtained by the product of its digits.

def get_product_of_digits(digits):
    if len(digits) == 0:
        return 0
    product = 1
    for each_digit in digits:
        product *= each_digit
    return product

number = int(input())
digits = list(map(int, str(number)))
print(get_product_of_digits(digits))