#Write a program that reads a distance D in km and calculates the score.
# For the first 50 km (0-50 km ), the score for each km is 3.
# For the next 50 km ( 51 - 100 km ), the score for each km is 5.
# For the next 100 km (101 - 200 km ), the score for each km is 6.
# For the distance above 200 km, the score for each km is 10.
# Apart from the above scores, there is a bonus score of 100.
d = int(input())

bonus = 100
if d <= 50:
    score = d * 3
elif d <= 100:
    score = 50 * 3 + (d - 50) * 5
elif d <= 200:
    score = 50 * 3 + 50 * 5 + (d - 100) * 6
elif d > 200:
    score = 50 * 3 + 50 * 5 + 100 * 6 + (d - 200) * 10
    
total_score = score + bonus
print(total_score)