#You are given some abbreviations as input. Write a program to print the acronyms separated by a dot(.) of those abbreviations.
words_list = input().split()

acronyms_list = []
for i in words_list:
    i = i[0]
    acronyms_list += [i]

output = ".".join(acronyms_list)
print(output)