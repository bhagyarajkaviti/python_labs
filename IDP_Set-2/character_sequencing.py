#Yash has a sequence of 26 distinct numbers P = (P1, P2, ..., P26), where the numbers from 1 to 26 are in random order. Ashok, one of Yash's friends, challenged him to construct a string S using the following table:
#Numbers   1 2 3 4 5 - - - - - 26
#Alphabets a b c d e - - - - - z
#Every number from 1 to 26 represents an alphabet as shown in above table.
#Yash should construct a string based on the alphabet numbers. Help Yash construct the string S.
#Write a program that reads the space-separated numbers and prints the resultant string S.

alpha = " abcdefghijklmnopqrstuvwxyz"
num_list = list(map(int,input().split()))
output = ""
for i in num_list:
    output += alpha[i]
print(output)