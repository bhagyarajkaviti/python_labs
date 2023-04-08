#Given a sentence S, write a program to print the frequency of each word in S. The output order should correspond with the word's input order of appearance.
#Input
#The input will be a single line containing a sentence S.
#Output
#The output contains multiple lines, with each line containing a word and its count separated by ": " with the order of appearance in the given sentence.

sentence_list = input().split(" ")
unique_words = []
for word in sentence_list:
    if word not in unique_words:
        unique_words.append(word)

for each_word in unique_words:
    msg = "{}: {}"
    print(msg.format(each_word, sentence_list.count(each_word)))







