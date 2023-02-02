#Given an amount, write a program to find the minimum number of notes of different denominations that sum up to the given amount. Available note denominations are 100, 50, 10, 1.
amount = int(input())

notes_100 = int(amount / 100)
print("100:" + str(notes_100))

notes_50 = int((amount % 100) / 50)
print("50:" + str(notes_50))

notes_10 = int(((amount % 100) % 50) / 10)
print("10:" + str(notes_10))

notes_1 = int((((amount % 100) % 50) %10)/ 1)
print("1:" + str(notes_1))



#amount = int(input())

#notes_100 = 0
#notes_50 = 0
#notes_10 = 0
#notes_1 = 0

#if amount >= 100:
    #notes_100 = int(amount / 100)
    #amount = (amount % 100)
    
#if amount >= 50:
    #notes_50 = int(amount / 50)
    #amount = (amount % 50)
    
#if amount >= 10:
    #notes_10 = int(amount / 10)
    #amount = (amount % 10)
    
#notes_1 = amount

#print("100:" + str(note_100))
#print("50:" + str(note_50))
#print("10:" str(note_10)) +
#print("1:" + str(note_1))