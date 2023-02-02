#Write a program to print the absolute difference between the two given numbers. (Absolute difference is the difference without the negative sign)
N1 = int(input())
N2 = int(input())

difference = N1 - N2  
if difference > 0:
    print(difference)
else:
    print((difference) * (-1))