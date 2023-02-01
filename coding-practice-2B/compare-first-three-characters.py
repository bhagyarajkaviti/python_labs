#Write a program to check if the first three characters in the two given strings are the same.
string1 = input()
string2 = input()
result = (string1[:3] == string2[:3])
print(result)