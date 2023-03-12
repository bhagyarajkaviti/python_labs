#A function is given in prefilled code that takes a number N as an argument.
#Write a program that checks if N is less than 1000.
#Return 5% of the N if N is less than 1000. Otherwise, return 10% of the N.
def calculate_percentage(number):
    # complete this function
    if number < 1000:
        percentage = number * 0.05
    else:
        percentage = number * 0.1
    return percentage


number = int(input())

result = calculate_percentage(number)# Call the calculate_percentage function

print(result)