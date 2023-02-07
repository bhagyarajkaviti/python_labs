#Given a word, write a program to print substrings in the expected pattern of N rows, where N is the length of the word.

string = input()

result = ""
for i in string:
    result = result + i
    print(result)
    
    
# or we can also write this manner


#for i in range(1, len(string)+1):
#    print(string[:i])