#Write a program that reads a distance D in km and calculates the total score.
# For the first 40 km (0-40 km ), the score for each km is 2.
# For the next 20 km (41 - 60 km ), the score for each km is 4.
#For the next 60 km ( 61 - 120 km ), the score for each km is 6.
#For the distance above 120 km, the score for each km is 8.
#Apart from the above scores, there is a bonus score of 50.
d = int(input())

bonus = 50
if d <= 40:
    score = d * 2
elif d <= 60:
    score = 40 * 2 + (d - 40) * 4
elif d <= 120:
    score = 40 * 2 + 20 * 4 + (d - 60) * 6
elif d > 120:
    score = 40 * 2 + 20 * 4 + 60 * 6 + (d - 120) * 8

total_score = score + bonus
print(total_score)