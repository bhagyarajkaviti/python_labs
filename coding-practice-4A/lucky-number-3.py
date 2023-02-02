#Write a program to print if the given number is divisible by any of the lucky numbers 6, 3, 2 in decreasing order of priority(6 is luckier than 3 and 3 is luckier than 2).
#Print "Number is divisible by" followed by the luckiest number among the above 3 which can divide the number.
#Print "Number is not divisible by 2, 3 or 6" if the number is not divisible by any of them.
number = int(input())

if (number % 6 == 0):
    print("Number is divisible by 6")
elif (number % 3 == 0):
    print("Number is divisible by 3")
elif (number % 2 ==0):
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")