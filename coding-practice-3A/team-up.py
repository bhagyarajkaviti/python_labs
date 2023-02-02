#Write a program that reads the scores A and B of two players and checks if one of the scores is greater than 300 and the sum of the scores is less than 500.
    #Print Can team up if one of the scores is greater than 300 and the sum of the scores is less than 500, otherwise print Cannot team up.
A = int(input())
B = int(input())

is_greater_than_300 = (A > 300 or B > 300)
is_sum_less_than_500 = (A + B) < 500

if is_greater_than_300 and is_sum_less_than_500:
    print("Can team up")
else:
    print("Cannot team up")