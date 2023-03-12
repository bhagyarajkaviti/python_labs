#Write a function with the name get_discount that takes the bill amount as an argument.
#- If the bill amount is less than 500, the discount should be "5%".
#- If the bill amount is greater than or equal to 500 and less than 2500, the discount should be "10%".
#- If the bill amount is greater than or equal to 2500, the discount should be "20%".
def get_discount(amount):
    # Complete this function
    if amount < 500:
        print("5%")
    elif amount >= 500 and amount < 2500:
        print("10%")
    else:
        print("20%")

amount = int(input())
get_discount(amount)
# Call the get_discount function
