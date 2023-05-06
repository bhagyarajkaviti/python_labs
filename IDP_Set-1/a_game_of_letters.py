#Sophia is given a sentence and asked to make every word in the sentence start with a vowel.
#In order to do this, she can rotate the letters in the words from left to right. Help Sophia update the words in the sentence.
#Write a program that reads the sentence and prints the updated sentence by performing the above operation.
#Note
#If there is no vowel in the word, then the letters will not rotate.
#Input
#The input will be a single line containing a string representing the sentence.


sentence = input().split()
vowels = ["a","e", "i", "o", "u"]
new_sentence = []
for word in sentence:
    new_word = word
    vowel_found = False
    for i in range(len(word)):
        if word[i].lower() in vowels:
            vowel_found = True
            new_word = word[i:]+word[:i]
            break
    new_sentence.append(new_word)
print(*new_sentence)