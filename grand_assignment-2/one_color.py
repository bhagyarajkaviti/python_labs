#Given a string of length N, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green. Find out the minimum number of characters you need to change to make the whole string of the same colour.
string = input()

red = 0
green = 0

for colour in string:
    if colour == "R":
        red = red + 1
    else:
        green = green + 1

if red > green:
    print(green)
else:
    print(red)