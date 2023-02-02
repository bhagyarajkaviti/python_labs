#The possible denominations of currency notes are 100, 50, 20 and 10. The amount A to be withdrawn is given as input. Write a program to break the amount into minimum number of bank notes.
amount = int(input())

if amount >= 100 or amount <= 100:
    notes_100 = int(amount / 100)
    amount = amount % 100
if amount >= 50 or amount <= 50:
    notes_50 = int(amount / 50)
    amount = amount % 50
if amount >= 20 or amount <= 20:
    notes_20 = int(amount / 20)
    amount = amount % 20
if amount >= 10 or amount <= 10:
    notes_10 = int(amount / 10)
    amount = amount % 10

print("100 Notes: " + str(notes_100))
print("50 Notes: " + str(notes_50))
print("20 Notes: " + str(notes_20))
print("10 Notes: " + str(notes_10))