#Write a program to find the minimum number of notes required for the amount M. Available note denominations are 500, 50, 10, 1.
amount = int(input())

if amount >= 500 or amount <= 500:
    notes_500 = int(amount / 500)
    amount = amount % 500
    
if amount >= 50 or amount <= 50:
    notes_50 = int(amount / 50)
    amount = amount % 50

if amount >= 10 or amount <= 10:
    notes_10 = int(amount / 10)
    amount = amount % 10

if amount >= 1 or amount <= 1:
    notes_1 = int(amount / 1)
    amount = amount % 1
    
print("500: " + str(notes_500) + " 50: " + str(notes_50) + " 10: " + str(notes_10) + " 1: " + str(notes_1))