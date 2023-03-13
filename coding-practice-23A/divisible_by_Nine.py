#A function is given in the prefilled code that takes three numbers N1, N2, and N3 as arguments.
#Write a program that returns True if atleast one of the given numbers N1, N2, and N3 is divisible by 9. Otherwise, return False.
def check_divisible_by_9(first_number, second_number, third_number):
    # complete this function
    if first_number % 9 == 0 or second_number % 9 == 0 or third_number % 9 == 0:
        msg = True
    else:
        msg = False
    
    return msg
        
first_number = int(input())
second_number = int(input())
third_number = int(input())

result = check_divisible_by_9(first_number, second_number, third_number)# Call the check_divisible_by_9 function

print(result)