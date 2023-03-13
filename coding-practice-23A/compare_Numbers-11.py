#A function is given in the prefilled code that takes two numbers M and N as arguments.
#Write a program that returns True if both the M and N are greater than 100 and M is less than N ....Otherwise, return False.
def compare_numbers(first_number, second_number):
    # complete this function
    if (first_number > 100 and second_number > 100) and (first_number < second_number):
        msg = True
    else:
        msg = False
        
    return msg

first_number = int(input())
second_number = int(input())

is_true = compare_numbers(first_number, second_number)# Call the compare_numbers function

print(is_true)