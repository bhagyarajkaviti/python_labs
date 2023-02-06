#Given a string S and N integers, where N is the length of the string S. Print the string after shuffling the characters as per the order of the integers given.
s = input()
len_of_s = len(s)
shuffled_s = ""

for i in range(len_of_s):
    index = int(input())
    shuffled_s = shuffled_s + s[index]

print(shuffled_s)