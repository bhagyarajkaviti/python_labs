#Write a program to check if the given string is a valid password or not. A string is considered as a valid password if the number of characters present is greater than 7.
password = input()
valid_password = (len(password) > 7)
print(valid_password)