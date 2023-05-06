#Disha has been given three strings A, B, and C consisting of lowercase alphabets, and a number T consisting of digits 1, 2, and 3.
#The teacher asked Disha to concatenate the three strings A, B, and C based on the order of digits in the given number T.
#• The digit 1 represented the string A.
#⚫ The digit 2 represented the string B.
#• The digit 3 represented the string C.
#Help Disha arrange the strings based on the order of digits in the given number T.
#Write a program that reads the strings A, B, C and a number T and prints the resultant string.

s1,s2,s3 = input(),input(),input()
words = [s1,s2,s3]
num_order = list(map(int,input()))

output = ""
for i in num_order:
    output += words[i-1]
print(output)