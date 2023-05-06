#In the World Boxing Championship, 14 matches will be held between Mary Kom and Amanda.
#Each match has three possible outcomes: Amanda can win, Mary Kom can win, or a draw can occur. If Amanda wins, she gets 2 points and Mary Kom gets 0 points. If Mary Kom wins, she gets 2 points and Amanda gets O points. If it's a draw, both of the players get 1 point.
#The total prize pool of the championship is 100 * X.
#After the 14 matches, the player who wins more matches than the other, will be declared as a champion and gets the prize money of 60 * X, whereas the loser gets the prize money of 40 * X.
#If both the players win same number of matches, then the defending champion Mary Kom is declared the winner and gets the prize money of 55 * X, whereas the loser gets the prize money of 45 * X.
#Your friend wants to find the prize money of Mary Kom. Your task is to determine the prize money of Mary Kom in the World Boxing Championship.
#Write a program that reads a number X representing the base prize pool and a string of length 14 consisting of the characters A, M, and D, representing the result of 14 matches. A denotes Amanda won the match, M denotes Mary Com won the match, and D denotes a draw and prints the total amount earned by Mary Kom.

n = int(input())
for i in range(n):
    x = int(input())
    string = input()
    if string.count("M") > string.count("A"):
        prize_money = 60 * x 
    elif string.count("M") == string.count("A"):
        prize_money = 55 * x
    else:
        prize_money = 40 * x
    print(prize_money)