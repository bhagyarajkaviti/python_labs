#Write a program to extract the numbers in a given string and print the sum, minimum and maximum of those numbers.
string = input()

numbers_list = []
for char in string:
    if char.isdigit():
        numbers_list += [int(char)]

print(sum(numbers_list))
print(min(numbers_list))
print(max(numbers_list))

#Another solution for the same question

#def get_digits(str_1):
#    digits_list = []
#    for char in str_1:
#        if (char.isdigit()):
#            digits_list += [int(char)]
#    return digits_list
#str_1 = input()
#digits_list = get_digits(str_1)
#sum_of_digits = sum(digits_list)
#print(sum_of_digits)
#min_of_digits = min(digits_list)
#print(min_of_digits)
#max_of_digits = max(digits_list)
#print(max_of_digits)