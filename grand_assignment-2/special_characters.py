#Write a program to count Vowels and Consonants in string.
string = input()
string = string.lower()

Vowels  = 0
Consonants = 0
for char in string:
    if char == " ":
        continue
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        Vowels = Vowels + 1
    else:
        Consonants = Consonants + 1

print(Vowels)
print(Consonants)