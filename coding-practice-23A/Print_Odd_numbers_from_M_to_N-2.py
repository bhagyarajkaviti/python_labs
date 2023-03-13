#A function is given in the prefilled code that takes two numbers M and N as arguments.
#Write a program to print all the odd numbers from Mto N separated by a space.
def get_odd_numbers_in_range(start_number, end_number):
    # complete this function
    output = ""
    for i in range(start_number, end_number+1):
        if i % 2 != 0:
            output += str(i) + " "
    
    return output

start_number = int(input())
end_number = int(input())

odd_numbers = get_odd_numbers_in_range(start_number, end_number)# Call the odd_numbers_in_range function

print(odd_numbers)