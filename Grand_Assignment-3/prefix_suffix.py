#Write a program to check the overlapping of one string's suffix with the prefix of another string.
#Input
#The first line of the input will contain a string A. The second line of the input will contain a string B.
#Output
#The output should contain overlapping word if present else print "No overlapping".
string_1 = input()
string_2 = input()

l1 = len(string_1)
output = ""
for char in string_2:
    if char in string_1:
        output += char
    else:
        break
        
l2 = len(output)
a = string_2[:l2]
b = output
if l2>0:
    if output[-1] != string_1[-1]:
        print(output[:-1])
    elif string_2[:l2] == output:
        print(string_2[:l2])
else:
    print("No overlapping")




#another SOLLUTION
#s1=input()
#s2=input()
#len_1=len(s1)
#len_2=len(s2)
#for i in range(1,(len_1)+1):
#    first=s1[-i:]
#    second=s2[:i]
#    if first==second:
#        break
#if first in s2:
#    print(first)
#else:
#    print("No overlapping")