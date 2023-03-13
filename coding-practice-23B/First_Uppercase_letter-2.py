#A function is given in the prefilled code that takes a string S as an argument.
#Write a program to return the first uppercase letter in the given string S.
def get_first_upper_letter(string):
    # complete this function
    for char in string:
        if char == char.upper():
            msg = char
            break
    
    return msg


string = input()
upper_case_character = get_first_upper_letter(string) # call the get_first_upper_letter function
print(upper_case_character)