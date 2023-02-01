#Write a program that reads two words A and B and checks if the second word B is the last part of the first word A.
word1 = input()
word2 = input()
result = ((word1[len(word1) - len(word2):]) == word2)
print(result)