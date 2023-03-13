#A function is given in the prefilled code that takes two numbers A and B as arguments.
#Write a program that compares the scores of A and B.
#Return "Win" if A is greater than B.
#Return "Draw" if A and B are equal.
#Return "Lose" if A is less than B.
def compare(team_a_points, team_b_points):
    # complete this function
    if team_a_points > team_b_points:
        msg = "Win"
    elif team_a_points == team_b_points:
        msg = "Draw"
    else:
        msg = "Lose"
    
    return msg

team_a_points = int(input())
team_b_points = int(input())

compare_result = compare(team_a_points, team_b_points) # Call the compare function

print(compare_result)