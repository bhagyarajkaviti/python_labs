#Given a string S and a number N, write a program to print the count of characters in S whose Unicode value is equal to the given number N.
string = input()
n = int(input())

count = 0
for char in string:
    unicode_value = ord(char)
    if unicode_value == n:
        count += 1
print(count)