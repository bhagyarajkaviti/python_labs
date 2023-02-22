#Given a string in camel case, write a python program to convert the given string from camel case to snake case.
snake_case = input()

camel_case = ""
for char in snake_case:
    if char == char.upper():
        camel_case = camel_case + "_" + char.lower()
    else:
        camel_case = camel_case + char

print(camel_case[1:])


# Another solution

#
#sentence = input()
#first_letter = sentence[0].lower()
#sentence = first_letter+sentence[1:]
#lower_case = ""
#for i in sentence:
#    upper = i.upper()
#    if i == upper:
#        lower_case += "_"
#    lower_case += i.lower()
#print(lower_case)