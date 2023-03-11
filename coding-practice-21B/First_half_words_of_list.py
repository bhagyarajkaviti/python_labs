#Given space-separated words, write a program that creates a list using space-separated words and prints the first half of the words in the list as a new list.
#Note:
#If the given number of words is an odd number, add one to it such that it becomes an even number and count half of the number of words.
words_list = input().split()
len_of_list = len(words_list)
half_length = int(len_of_list / 2)
if len_of_list % 2 == 0:
    print(words_list[:half_length])
else:
    print(words_list[:half_length + 1])