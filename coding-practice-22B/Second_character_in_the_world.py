#For this problem, the prefilled code will contain a function. Write a program that the given function will return the second character in the word passed to the function.
def second_character(arg_1):
    # Complete this function
    second_char = arg_1[1]
    return second_char

word = input()
# Call the second_character function
result = second_character(word)
print(result)