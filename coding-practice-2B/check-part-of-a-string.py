#write a program that reads two words A, B, and an index I. check if B starts at index I in A.
word1 = input()
word2 = input()
index = int(input())
result = (word1[index:len(word2) + index] == word2)
print(result)