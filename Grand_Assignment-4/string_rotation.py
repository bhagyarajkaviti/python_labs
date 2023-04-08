#Given two strings (S1 and S2), write a program to determine if a string S2 is a rotation of another string S1.
#Input
#The first line of the input will be a string S1. The second line of the input will be a string S2.
#Output
#If string S2 is a rotation of another string S1, print number of right rotations made by string S1 to match the string S2. Otherwise, print "No Match".
#Where right rotation means all elements are moving towards the right side by one place where the last element will be placed in the first place example, one right rotation of "python" is "npytho".

string1 = input()
string2 = input()

count = 0
for char in string1:
    if char in string2:
        count += 1
    

if count == len(string2):
    if string1[0] in string2:
        index = string2.index(string1[0]) 
        print(index)
else:
    print("No Match")
