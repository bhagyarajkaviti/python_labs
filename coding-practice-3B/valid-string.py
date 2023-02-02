#Write a program that reads a string S and checks if the length of S is between 2 and 7 or the first character of S is not equal to "a".
    #Print Valid String if the length of S is between 2 and 7 or the first character of S is not equal to "a". Otherwise, print Not a Valid String.
word = input()

length = len(word)

length_validation = length > 2 and length < 7
character_validation = word[0] != "a"

if length_validation or character_validation:
    print("Valid String")
else:
    print("Not a Valid String")