#Write a program to check whether the given password is valid or not. Consider the password to be valid if it contains at least one uppercase letter, one lowercase letter, and one digit.
password = input()
contains_digit = False

for character in password:
  is_digit = character.isdigit()
  if is_digit:
    contains_digit = True
    
is_all_lower = (password.lower() == password)
is_all_upper = (password.upper() == password)
contains_lower_and_upper = (not is_all_lower) and (not is_all_upper)

is_valid_password = (contains_digit and contains_lower_and_upper)

if is_valid_password:
    print("Valid Password")
else:
    print("Invalid Password")




#the solution written below passed only 7 testcases out of 10 .

#password = input()

#x = False
#y = False
#z = False
#for i in password:
#    if i == i.upper():
#       x = True
#    else:
#        x = False
#    if i == i.lower():
#        y = True
#    else:
#        y = False
#    digit = i.isdigit()
#    if digit:
#        z = True
#    else:
#        z = False
#if ((x and y) and z):
#    print("Valid Password")
#else:
#    print("Invalid Password")
    