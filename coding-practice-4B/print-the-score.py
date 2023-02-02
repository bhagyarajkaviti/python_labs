#Write a program that reads a distance D in km and calculates the score.
    # If D is less than or equal to 10, the score is D.
    # If D is greater than 10, the score is the sum of 10 and (D - 10) * 3.
distance = int(input())
    
if distance <= 10:
    print(distance)
else:
    score = 10 + (distance - 10) * 3
    print(score)