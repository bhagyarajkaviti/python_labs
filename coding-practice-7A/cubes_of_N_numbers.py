#Write a program that reads a number N and prints the cube of N numbers from 1.
#Note: The cube of a number X is X to the power of 3. (x3)
n = int(input())

count = 1
while count <= n:
    print(count ** 3)
    count += 1