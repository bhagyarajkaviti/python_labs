#You are given a string, write a program to find whether the string is palindrome or not.
#Note: Treat uppercase letters and lowercase letters as same when comparing letters.
word = input()
word = word.lower()

reverse_word = ""
for i in word:
    reverse_word = i + reverse_word
    
is_palindrome = word == reverse_word

print(is_palindrome)