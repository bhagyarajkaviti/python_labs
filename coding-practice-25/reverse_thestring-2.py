#A function is given in the prefilled code that takes a string S as an argument.
#Write a program that returns the reverse of the given string S using Recursion.

#def get_reversed_string(string):
#    reverse_string = string[::-1]
#    return reverse_string

#string = input()

#resultant_string =get_reversed_string(string) # Call the get_reversed_string function
#print(resultant_string)




#Using Recursion


def get_reversed_string(string):
    if len(string) == 1:
        return string[0]
        
    return string[len(string) - 1] + get_reversed_string(string[:-1])
    
string = input()

resultant_string = get_reversed_string(string)
print (resultant_string)
