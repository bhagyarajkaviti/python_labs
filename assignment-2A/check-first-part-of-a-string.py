#Write a program that reads two strings S1 and S2, and checks if S2 is the first part of S1.
string1 = input()
string2 = input()

result = (string2 == string1[:len(string2)])

print(result)