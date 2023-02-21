#Write a program to find the first upper case letter in the given string.
string = input()

for i in string:
    if i == i.upper():
        if not i.isdigit():
            #print(i)
            break
print(i)