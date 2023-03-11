#Given a sentence S. The words in the sentence S are separated by a space.
#Write a program that prints a new string by joining the third letter of each word in the sentence with the comma(, ).
sentence_list = input().split()

output = []
for i in sentence_list:
    if (len(i) > 2):
        char = i[2]
        output += [char]

final_output = ",".join(output)
print(final_output)