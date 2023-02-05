#Write a program to check whether the given password is valid or not. Consider the password to be valid if it contains at least one uppercase letter.
password = input()

x = False
for i in password:
    if i == i.upper():
        x = True
if x:
    print("Valid Password")
else:
    print("Invalid Password")
    
# Another solution for this Question

#password = input()

#is_all_lower = (password.lower() == password)

#if is_all_lower:
#    print("Invalid Password")
#else:
#    print("Valid Password")