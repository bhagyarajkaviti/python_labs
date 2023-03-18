#For this problem, the prefilled code will contain a function. Write a program to count the number of uppercase and lowercase letters in the given word.
def count_of_lowercase_and_uppercase_letters(arg_1):
    # Complete this function
    count_of_lowercase = 0
    count_of_uppercase = 0
    for i in arg_1:
        if i == i.upper():
            count_of_uppercase += 1
        if i == i.lower():
            count_of_lowercase += 1
    print(count_of_uppercase)
    print(count_of_lowercase)


word = input()
count_of_lowercase_and_uppercase_letters(word)
