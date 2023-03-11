#Given a sentence, write a program to reverse the letters in words of the sentence.
sentence_list = input().split()

output_list = []
for word in sentence_list:
    word = word[::-1]
    output_list += [word]
output_sentence = " ".join(output_list)
print(output_sentence)