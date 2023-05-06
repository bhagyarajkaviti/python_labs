#A shopkeeper records all purchases at the end of the day. He has prices for all the purchases that happened at the shop today. He wants to know which item got sold only once and which item got sold more than once.
#Write a program that reads the space-separated prices and prints the price of items that sold only once and more than once.
#Note
#In the case of ties, choose the price of the item that was sold earlier in the day.


price_list = list(map(int, input().split()))

for i in price_list:        
    single_sold =  None
    if price_list.count(i) == 1:
        single_sold = i
        break
print(single_sold)

for i in price_list:
    multi_sold =  None
    if price_list.count(i) > 1:
        multi_sold =  i
        break
print(multi_sold)
