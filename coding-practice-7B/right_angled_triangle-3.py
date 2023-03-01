#Write a program that reads a number N and prints a Right Angled Triangle of N rows using stars (*) and pluses ( + ).
#The first N-1 rows contains stars ( contains pluses ( + ). ) and the Nth row
#   *
#   * *
#   + + +
rows = int(input())

count = 1
while count <= rows:
    if count == rows:
        print("+ " * count)
    else:
        print("* " * count)
    count += 1