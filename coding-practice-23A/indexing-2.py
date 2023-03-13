#For this problem, the prefilled code will contain a function. Write a program that the given function will return the character present at the index N in the word W.
def indexing(arg_1, arg_2):
    # Complete this function
    character = arg_1[arg_2]
    print(character)

word = input()
index = int(input())
# Call the indexing function
indexing(word, index)