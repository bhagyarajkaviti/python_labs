#Given a string, write a program to check if it is a palindrome or not. Palindrome is a string that remains the same when written in reverse. Note: Ignore the case difference (uppercase and lowercase) when comparing letters.
word = input()
word_lower = word.lower()

palindrome = ""
for i in word:
    palindrome = i + palindrome 
palindrome_lower = palindrome.lower()

if word_lower == palindrome_lower:
    print("Palindrome")
else:
    print("Not a Palindrome")
    