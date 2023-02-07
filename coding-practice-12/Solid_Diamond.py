#Write a program to print a solid diamond pattern of 2N - 1 rows using the asterisk character (*).
n = int(input())

for i in range(1 , n+1): #Part 1: Upto nth row in accending order of asterisk(*)
    star = " " * (n - i) + "* " * i
          # Left space #
    print(star)
for i in range(1 , n): #part 2: from (n+1)th row to (2n -1)th row in decending order of asterisk(*)
    star2 = " " * i + "* " * (n - i)
    print(star2)