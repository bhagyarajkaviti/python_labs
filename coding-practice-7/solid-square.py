#Write a program to print a solid square pattern of N rows and N columns using the asterisk character (*), where integer N is given as an input.
integer = int(input())

count = 1

while count <= integer:
    print("* " * integer)
    count = count + 1