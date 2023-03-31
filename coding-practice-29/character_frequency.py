#Write a program to compute the frequency of characters other than space.
#Input
#The input will be a single line containing a string.
#Note:
#1. The input string will contain only alphabets and white space.
#2. Ignore the case-sensitivity.
#Output
#The output should be M lines equal to unique characters in the given string sorted in alphabetical order. Each line should contain the character and its frequency separated by a colon (:).
def char_frequency(string):
    string = string.lower()
    unique_Chars = set(string)
    unique_Chars.discard(' ')
    unique_Chars = sorted(unique_Chars)
    for char in unique_Chars:
        output = "{}: {}"
        print(output.format(char, string.count(char)))
    
    
string = input()
char_frequency(string)