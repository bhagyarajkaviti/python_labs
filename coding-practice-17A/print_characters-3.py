#Given a number N, write a program that reads N Unicode values and prints a string by joining the characters of given N Unicode values.
n = int(input())

word = ""
for i in range(n):
    unicodes = int(input())
    word += chr(unicodes)
print(word)