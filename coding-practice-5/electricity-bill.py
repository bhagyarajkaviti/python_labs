#In this problem, you need to write a program to calculate the electricity bill for a household, based on the units of electricity the household consumed. The price for unit varies based on the slab.
#The charges per unit for different slabs are as mentioned below:
    #For the first 50 units (0-50), the charge is 2/unit
    #For the next 100 units (51-150), the charge is 3/unit
    #For the next 100 units (151-250), the charge is 5/unit
    #For above 250 units (251 and above), the charge is 8/unit
#Apart from these charges, there is also an additional surcharge of 20% on the total amount is added to the bill.
units = int(input())

if units <= 50:
    charge1 = units * 2
    total = charge1 * 1.2
if 50 < units <= 150:
    charge1 = 50 * 2
    charge2 = (units - 50) * 3
    total = (charge1 + charge2) * 1.2
if 150 < units <= 250:
    charge1 = 50 * 2
    charge2 = 100 * 3
    charge3 = (units - 150) * 5
    total = (charge1 + charge2 + charge3) * 1.2
if units > 250:
    charge1 = 50 * 2
    charge2 = 100 * 3
    charge3 = 100 * 5
    charge4 = (units - 250) * 8
    total = (charge1 + charge2 + charge3 + charge4) * 1.2
print(total)

#units = int(input())

#bill = Ө

#if units < 50:
    #bill = 2 * units
#elif units < 150:
    #bill = (2 * 50) + (3* (units - 50))
#elif units < 250:
    #bill = (2 * 50) + (3 * 100) + (5) * (units - 150))
#elif units >= 250:
    #bill = (2 * 50) + (3 * 100) + (5 * 100) + (8 * (units - 250))
    
#surcharge = (0.2* bill)

#total_bill = (bill + surcharge)

#print(total_bill)