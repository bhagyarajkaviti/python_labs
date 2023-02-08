#Write a program that reads a distance D in km and calculates the total score.
 #For the first 50 km (0-50 km ), the score for each km is 3.
 #For the distance above 50 km, the score for each km is 5.
distance = int(input())

if distance <= 50:
    score = distance * 3
else:
    score = 50 * 3 + (distance - 50) * 5
    
print(score)