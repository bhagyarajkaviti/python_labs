#A function is given in prefilled code that takes a string S as an argument.
#Write a program that prints the count of uppercase letters in the given string S
def count_of_uppercase(word):
    # complete this function
    count = 0
    for char in word:
        if char == char.upper():
            count += 1
        
    return count

word = input()

result = count_of_uppercase(word)# Call the count_of_uppercase function

print(result)