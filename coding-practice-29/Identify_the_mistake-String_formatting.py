#Given two strings, name and sport. Write a program using string formatting to concatenate the name followed by the message "is playing" and followed by the sport.
str_a = input()
str_b = input()
message = "{arg_1} is playing {arg_2}"
print(message.format(arg_2=str_b, arg_1=str_a))
