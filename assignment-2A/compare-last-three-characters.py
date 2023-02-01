#write a program to check if the last three haracters in the two given strings are the same.
word1 = input()
word2 = input()

result = (word1[len(word1) - 3:] == word2[len(word2) - 3:])
print(result)