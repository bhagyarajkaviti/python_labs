#Write a program that reads two numbers M and N, and prints a Rectangle of M rows and N columns using stars ( ).
#   *****
#   *****
#   *****
#   *****
rows = int(input())
columns = int(input())

count = 1
while count <= rows:
    print("*" * columns)
    count += 1