#Write a program that resds a word and checks if the first letter and last letter of the word are not the same.
word = input()
result = (word[0] != word[len(word) - 1])
print(result)