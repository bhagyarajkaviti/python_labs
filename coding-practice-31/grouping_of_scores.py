#A player has collected few colored balls which have a number on them.
#To calculate score, we have to group the colored balls picked by user and sum up the numbers on them.
#Write a program to create a dictionary, grouping of colored balls and the corresponding total score.
#Input
#The input will be a single line containing comma-separated key-value pairs.
#Each key-value pair is separated by the colon character (:).
def get_ball_score_dict(ball_color_score_list):
    ball_color_score_dict = {}
    for ball_details in ball_color_score_list:
        ball_details_list = ball_details.split(":")
        ball_color, ball_score = ball_details_list[0], int(ball_details_list[1])
        if ball_color in ball_color_score_dict:
            score = ball_color_score_dict[ball_color]
            total_score = ball_score + score
            ball_color_score_dict[ball_color] = total_score
        else:
            ball_color_score_dict[ball_color] = ball_score
    return sorted(ball_color_score_dict.items())

ball_color_score_list = input().split(",")
ball_color_score_dict = get_ball_score_dict(ball_color_score_list)
print(ball_color_score_dict)