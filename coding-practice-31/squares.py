#Write a program to create a dictionary that contains keys as numbers from 1 to N and values are square of keys.
#Input
#The input will be a single line containing an integer (N).
#Output
#The output should be a single line containing the dictionary with key- value pairs from 1 to N.
n = int(input())
square_dict = {}
for i in range(1,n+1):
    square_dict[i] = i**2
print(square_dict)