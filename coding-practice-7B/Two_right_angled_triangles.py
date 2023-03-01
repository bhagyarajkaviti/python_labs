#Write a program that reads a number N and prints two Right Angled Triangles of N rows, using numbers starting from 1.
#1
#22
#333
#1
#22
#333
rows = int(input())

count = 1
while count <= rows:
    print(str(count) * count)
    count += 1
    
count = 1
while count <= rows:
    print(str(count) * count)
    count += 1