#A function is given in prefilled code that takes a string S as an argument.
#Write a program that checks if the given string S is valid.
#Return Valid String if the first character of S is a digit or the number of characters present in S is greater than or equal to 6. Otherwise, return Invalid String.
def valid_string(string):
    # complete this function
    length = len(string)
    first_char = string[0]
    if first_char.isdigit() or length >= 6:
        output = "Valid String"
    else:
        output = "Invalid String"
    return output

string = input()

result = valid_string(string)# Call the valid_string function

print(result)