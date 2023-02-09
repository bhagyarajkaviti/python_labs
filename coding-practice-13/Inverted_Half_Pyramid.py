#Write a program to print the inverted half pyramid pattern up to the given N number of rows.

n = int(input())
k = n
for i in range(1, n + 1):
    output = ""
    for j in range(1, k + 1):
        output = output + str(j) + " "
    print(output)
    k = k -1
    
    
    
#number = int(input())
 
#for i in range(number):
#    pattern = ""
#    k = number - i
#    for j in range(1, k+1):
#        pattern = pattern + (str(j) + " ")
#    print (pattern)