#Write a program to print a triangular pattern with numbers in N rows , where integer N is given as input.
num = int(input())

for row_num in range(1, num + 1):
    row_out = ""
    for seq_num in range(1, row_num + 1):
        row_out = row_out + str(seq_num) + " "
    
    print(row_out)