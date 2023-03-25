#Write a program to convert a list into a tuple.
#The input will be a single line containing the comma-separated integers.
#The output should be a single line containing the tuple with the list elements.
str_a = input()
a = str_a.split(",")
i = 0
for item in a:
    a[i] = int(item)
    i += 1
print(tuple(a))
