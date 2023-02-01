word = input()
word_length = len(word)
stars = word_length - 4
result = word[:2] + "*" * (stars) + word[word_length - 2:]
print(result)
#print(word[:2] + "*" * (len(word) - 4) + word[len(word) -2:])