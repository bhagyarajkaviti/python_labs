#Given an amount, write a program to find a minimum number of currency notes of different denominations that sum to the given amount. Available note denominations are 1000, 500, 100, 50, 20, 5, 1.
amount = int(input())

if amount >= 1000 or amount <= 1000:
    notes_1000 = (int(amount / 1000))
    amount = amount % 1000
if amount >= 500 or amount <= 500:
    notes_500 = (int(amount / 500))
    amount = amount % 500
if amount >= 100 or amount <= 100:
    notes_100 = (int(amount / 100))
    amount = amount % 100
if amount >= 50 or amount <= 50:
    notes_50 = (int(amount / 50))
    amount = amount % 50
if amount >= 20 or amount <= 20:
    notes_20 = (int(amount / 20))
    amount = amount % 20
if amount >= 5 or amount <= 5:
    notes_5 = (int(amount / 5))
    amount = amount % 5
if amount >= 1 or amount <= 1:
    notes_1 = (int(amount / 1))
    
print("1000:" + str(notes_1000))
print("500:" + str(notes_500))
print("100:" + str(notes_100))
print("50:" + str(notes_50))
print("20:" + str(notes_20))
print("5:" + str(notes_5))
print("1:" + str(notes_1))