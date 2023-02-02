#Write a program to find the minimum number of notes required for the amount M. Available note denominations are 2000, 500, 200, 50, 20, 5, 2, 1.
amount = int(input())

if amount >= 2000 or amount <= 2000:
    notes_2000 = int(amount / 2000)
    amount = amount % 2000
if amount >= 500 or amount <= 500:
    notes_500 = int(amount / 500)
    amount = amount % 500
if amount >= 200 or amount <= 200:
    notes_200 = int(amount / 200)
    amount = amount % 200
if amount >= 50 or amount <= 50:
    notes_50 = int(amount / 50)
    amount = amount % 50
if amount >= 20 or amount <= 20:
    notes_20 = int(amount / 20)
    amount = amount % 20
if amount >= 5 or amount <= 5:
    notes_5 = int(amount / 5)
    amount = amount % 5
if amount >= 2 or amount <= 2:
    notes_2 = int(amount / 2)
    amount = amount % 2
if amount >= 1 or amount <= 1:
    notes_1 = int(amount / 1)
    amount = amount % 1
print("2000:" + str(notes_2000) + " 500:" + str(notes_500) + " 200:" + str(notes_200) + " 50:" + str(notes_50) + " 20:" + str(notes_20) + " 5:" + str(notes_5) + " 2:"+ str(notes_2) + " 1:" + str(notes_1))