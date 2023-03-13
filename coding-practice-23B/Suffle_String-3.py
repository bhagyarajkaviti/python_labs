#A function is given in the prefilled code that takes a string S and N space-separated indices as an argument.
#Write a program that prints a string by joining characters present at each index of the given N indices.
def shuffle_string(string, indexes_list):
    # complete this function
    index_list = indices_list.split()
    output = ""
    for i in index_list:
        i = int(i)
        output += string[i]
        
    return output

string = input()
indices_list = input()

result = shuffle_string(string, indices_list) # call the shuffle_string function
print(result)