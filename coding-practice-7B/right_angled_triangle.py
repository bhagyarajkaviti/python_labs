#Write a program that reads a number N and prints a Right Angled Triangle of N rows using stars ( * ).
#   *
#   **
#   ***
#   ****
rows = int(input())

count = 1
while count <= rows:
    print("*" * count)
    count += 1