#Your friend is hosting a game with N players. The players are seated around a circular table in chairs numbered from 1 to N.
#At the beginning of the game, the host randomly chooses a chair number S among the chairs numbered from 1 to N.
#Beginning with the player in chair S, one chocolate will be handed to each player sequentially around the table until all of the M pieces of chocolates have been distributed.
#The player who receives the last chocolate wins this game. Help your friend to find who is going to win.
#Write a program that reads the N number of players, M pieces of chocolates and the randomly choosen chair number S and prints the chair number of the player who received the last chocolate.

n = int(input())
for i in range(n):
    students, choco, start = map(int,input().split())
    start = start - 1
    student_list = list(range(1,students+1))
    new_pattern = student_list[start:] + student_list[:start]
    #print(new_pattern)
    end = choco % students - 1
    print(new_pattern[end])