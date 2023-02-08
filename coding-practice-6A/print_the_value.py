#Write a program that reads a string S. The string S contains a number except the last character. The last character of the string contains T or H or K.
#Print the Value by multiplying the number in S with 10 or 100 or 1000 based on the last character.
#Last Character              Represents                  Value
#    T                           Tens              Multiply the number in string with 10
#    H                          Hundreds           Multiply the number in string with 100
#    K                          Thousands          Multiply the number in string with 1000
s = input()

length = len(s)
number = int(s[:length - 1])
alphabet = s[length - 1]

if alphabet == "T":
    print(number * 10)
elif alphabet == "H":
    print(number * 100)
elif alphabet == "K":
    print(number * 1000)