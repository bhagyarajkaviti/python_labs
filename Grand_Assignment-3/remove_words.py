#Given a string, write a program to remove all the words with K length.
#Input
#The first line of the input will contain a string A. The second line of the input will contain an integer K.
#Output
#The output should contain a string after removing all the words whose length is equal to K.
#Explanation
#For example, string A is "Tea is good for you", k is 3 then output should be "is good." Here words "Tea", "for", "you" length is equal to 3, so these words are removed from string.

string_list = input().split(" ")
n = int(input())

l = len(string_list)

output = ""
for each_word in string_list:
    if len(each_word) != n:
        output += each_word + " "

print(output)