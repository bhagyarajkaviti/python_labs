#Abhinav and Anjali are playing Rock-Paper-Scissors game. Rock- Paper-Scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock", "paper" and "scissors". 
#Based on the shapes the player chooses the outcome of the game is determined. A rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it. If the same shape is chosen by both of the players, then it is tie. Write a program to decide the winner of each round of the game based on the shapes the players chose.
#Input
    #The first line of input will be one of the strings "Rock", "Paper", "Scissors", representing the shape chosen by Abhinav. The second line of input will be the sting representing the shape chosen by Anjali..
#Output
    #The output should either be "Abhinav Wins" or "Anjali Wins", based on the winner. If it is a tie, the output should be "Tie".
Abhinav = input()
Anjali =input()
    
if Anjali == Abhinav:
    print("Tie")
else:
    if Abhinav == "Rock" and Anjali == "Paper":
        print("Anjali Wins")
    elif Abhinav == "Scissors" and Anjali =="Rock":
        print("Anjali Wins")
    elif Abhinav == "Paper" and Anjali == "Scissors":
        print("Anjali Wins")
    else:
        print("Abhinav Wins")