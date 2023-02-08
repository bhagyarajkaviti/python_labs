#Write a program that reads a distance D in km and calculates the total score.
# For the first 20 km (0-20 km ), the score for each km is 2.
# For the next 40 km (21-60 km ), the score for each km is 4.
# For the distance above 60 km, the score for each km is 6.
# Apart from the above scores, there is a bonus score of 30.
d = int(input())
bonus = 30
if d <= 20:
    score = d * 2
elif d <= 60:
    score = 20 * 2 + (d - 20) * 4
elif d > 60:
    score = 20 * 2 + 40 * 4 + (d - 60) * 6

print(score + bonus)