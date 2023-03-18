#Write a function with the name calculate_bill that takes the bill amount as an argument.
#- If the bill amount is less than 500, the discount should be 5%.
#- If the bill amount is greater than or equal to 500 and less than 2500, the discount should be 10%.
#- If the bill amount is greater than or equal to 2500, the discount should be 20%.
#Calculate the bill amount with the appropriate discount and print it.
def calculate_bill(amount):
    if amount < 500:
        amount = amount * 95/100
        return amount
    elif amount >= 500 and amount < 2500:
        amount = amount * 90/100
        return amount
    else:
        amount = amount * 80/100
        return amount

amount = int(input())
result = calculate_bill(amount)
print(result)

