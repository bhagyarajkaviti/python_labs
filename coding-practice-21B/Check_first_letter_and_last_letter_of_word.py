#Given space-separated words, write a program to check if the first letter and last letter of each word are the same.
#Note: Consider both uppercase and lowercase letters as the same.
sentence = input().lower()
words_list = sentence.split()

for word in words_list:
    if word[0] == word[-1]:
        print(True)
    else:
        print(False)