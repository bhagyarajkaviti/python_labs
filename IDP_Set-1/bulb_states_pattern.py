#Bulb states pattern
#In a building, there are N rooms numbered from 1 to N. Each room has a bulb that is initially ON for even-numbered rooms and OFF for odd-numbered rooms.
#Your task is to note the status of the bulb after entering a room. When you leave a room, turn OFF the bulb if it is ON and turn ON the bulb if it is OFF. Visit all rooms in the same order as they are numbered and then return to the starting room and repeat the process N times.
#Write a program that reads the N rooms and prints the status of the bulb for each room after completing each visit.
#Note
#Print 1 if the bulb is ON, 0 otherwise

n = int(input())
matrix = []
for i in range(1, n +1):
    if i % 2 == 1:
        row = []
        for j in range(1,n+1):
            if j % 2 == 1:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    else:
        row = []
        for j in range(1,n+1):
            if j % 2 == 1:
                row.append(0)
            else:
                row.append(1)
        matrix.append(row)

for i in matrix:
    print(*i)