#You are given a string, write a program to find whether the string is palindrome or not.
#Note: Treat uppercase letters and lowercase letters as same when comparing letters. Ignore spaces and quotes within the string.
string = input()
string = string.replace(" ", "")
string = string.replace("'", "")
string = string.lower()

reverse_string = ""
for i in string:
    reverse_string = i + reverse_string

is_palindrome = reverse_string == string

print(is_palindrome)


# Alternate Solution for the same question.

#str1 = input()
#str1 = str1.casefold()
#str1 = str1.replace(" ","")
#str1 = str1.replace("'","")

#if (str1 == str1[::-1]):
#    print("True")
#else:
#    print("False")