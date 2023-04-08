#Given a sentence S, write a program to print the frequency of each word in S, where words are sorted in alphabetical order.
#Input
#The input will be a single line containing a string S.
#Output
#The output contains multiple lines, with each line containing a word and frequency of each word in the given string separated by ":", where words are sorted in alphabetical order.

sentence_list = input().split(" ")

words_set = set(sentence_list)
unique_words = sorted(words_set)
for each_word in unique_words:
    msg = "{}: {}"
    print(msg.format(each_word, sentence_list.count(each_word)))