#Write a program that reads two coupon codes A and B and checks if the first three characters of one of the coupon codes is equal to "DIS".
#Print Discount if the first three characters of one of the coupon codes is equal to "DIS". Otherwise, print No Discount.
A = input()
B = input()

condition = (A[:3] == "DIS") or (B[:3] == "DIS")

if condition:
    print("Discount")
else:
    print("No Discount")