#For this problem, the prefilled code will contain a dictionary. Write a program to remove N key-value pairs from the dictionary if they present.
#Input
#The input will be a single line containing space-separated strings, denoting the keys.
#Output
#The output should be a single line containing the dictionary without the given key-value pairs.

alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
}

# Write your code here
remove_keys = input().split()
for each_key in remove_keys:
    if each_key in  alphabets:
        del alphabets[each_key]
    
print(alphabets)