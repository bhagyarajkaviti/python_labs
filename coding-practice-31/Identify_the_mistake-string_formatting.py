#Given two strings, name and sport. Write a program using string formatting to concatenate the name followed by the message "is playing" and followed by the sport.
#Input
#The first line of input will contain a string. The second line of input will contain a string.
#Output
#The output should be a single line concatenating the message with the given inputs.

str_a = input()
str_b = input()
message = "{arg_1} is playing {arg_2}"
print(message.format(arg_1=str_a, arg_2=str_b))
