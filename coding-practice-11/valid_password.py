#Write a program to check whether the given password is valid or not. Consider the password to be valid if it contains at least one digit.
password = input()
x  =  False
for  i  in password:
    is_digit = i.isdigit()
    if is_digit:
        x = True
if x:
    print("Valid Password")
else:
    print("Invalid Password")