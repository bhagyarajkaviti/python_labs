#Write a program to print the inverted half pyramid pattern up to the given N number of rows.
# Identify the Mistake - inverted Half Pyramid - 2

#n = int(input())

#for row_num in range(0,n+1):
#    row_output = ""
#    seq_num = row_num
#    while seq_num > 0:
#        row_output = row_output + str(seq_num)
#        seq_num = seq_num - 1
#    print(row_output)
    
    
#Corrected solution
n = int(input())

for row_num in range(0,n):
    row_output = ""
    seq_num = n - row_num
    while seq_num > 0:
        row_output = row_output + str(seq_num)
        seq_num = seq_num - 1
    print(row_output)
