#There is an English competition in which players are divided into N groups, each group having 2 players.
#As part of the competition, each player in a group selects a word. The group will be eligible for the next round if they are able to rearrange the letters in the first player's word to form the second player's word. Your task is to check whether the group is eligible for the next round or not.
#Write a program that reads the N groups of two space-separated words and checks if the players are able to rearrange the letters in the first player's word to form the second player's word in each group.
#Note
#All characters in the input will be in lowercase.

n = int(input())

output = []
for i in range(n):
    word1, word2 = input().split()
    count = 0
    if len(word1) == len(word2):
        for char in word2:
            if char in word1:
                count += 1
    if count == len(word2):
        output.append("YES")
    else:
        output.append("NO")
    
print(*output)