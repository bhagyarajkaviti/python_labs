#Given a word, write a program to convert all the uppercase letters to lowercase letters and vice versa.
word = input()

swap = word.swapcase()
print(swap)


#the program written below is without .swapcase() string method.

#word = input()
#modified_word = ""
#for character in word:
#    uppercase_char = character.upper()
#    if uppercase_char == character: 
#        modified_word = modified_word + character.lower()
#    else:
#        modified_word = modified_word + character.upper()
#print (modified_word)