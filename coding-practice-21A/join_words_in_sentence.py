#Given a sentence S. The words in the sentence S are separated by a space.
#Write a program that prints a string by joining the words in the sentence S with the dot( . ).
sentence_list = input().split()
sentence_modified = ".".join(sentence_list)
print(sentence_modified)