#Abhinav and Anjali are playing the Tic-Tac-Toe game. Tic-Tac-Toe is a game played on a grid that's three squares by three squares. Abhinav is O, and Anjali is X. Players take turns putting their marks in empty squares. The first player to get 3 of her marks in a diagonal or horizontal, or vertical row is the winner. When all nine squares are complete, the game is over. If no player has three marks in a row, the game ends in a tie. Write a program to decide the winner in the Tic- Tac-Toe game.
#Input
#The input will be three lines contain O's and X's separated by space.
#Output
#The output should be a single line containing either "Abhinav Wins" or "Anjali Wins" or "Tie".


board = []      
for i in range(3):
    line = input().split()
    board.append(line)

if (board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O") or (board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O")   or  (board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O") or (board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O") or (board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O") or (board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O") or (board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O") or (board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O"):
        print("Abhinav Wins")    

elif (board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X") or (board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X")   or  (board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X") or (board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X") or (board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X") or (board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X") or (board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X") or (board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X"):
        print("Anjali Wins")    
else:
    print("Tie")