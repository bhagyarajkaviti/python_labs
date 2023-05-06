#There are N pyramids in a line. Given their heights, your task is to find the minimum absolute difference between the heights of any two different pyramids.
#Write a program that reads the N space-separated heights of the pyramids and prints the minimum absolute difference between the heights of any two different pyramids.
#Input
#The input will be a single line containing space-separated integers representing the heights of the N pyramids.
#Output
#The output should be a single line containing the minimum absolute difference between the heights of any two different pyramids.

heights = list(map(int, input().split()))
#print(heights)
heights_set = set(heights)
#print(heights_set)
difference = []
for i in heights:
    a = {i}
    remain = heights_set - a
    for j in remain:
        difference.append(abs(i - j))

if len(difference)>0:
    print(min(difference))
else:
    print(0)