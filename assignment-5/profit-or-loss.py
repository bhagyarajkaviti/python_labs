#The amount at which a product is sold by the seller is known as the Selling Price. The amount at which the seller has acquired the product is known as the Cost Price.
#If the Selling Price of a product is higher than its cost price, then the seller has made a profit. If it is lesser, then the seller has incurred loss selling that product. If the Selling Price is equal to the Cost Price, it means the seller has made No Profit and No loss, by selling the product.
#Given Cost price CP and selling price SP of a product, write a program to determine whether the seller made a profit, incurred loss, or made no profit or loss.
CP = int(input())
SP = int(input())

profit = SP - CP
loss = CP - SP
no_profit_no_loss = CP == SP

if profit > 0:
    print("Profit")
elif loss > 0:
    print("Loss")
else:
    print("No Profit - No Loss")