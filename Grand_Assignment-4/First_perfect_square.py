#Given two integers (M and N), write a program to print the first perfect square in a given range.
#Input
#The first line of input will contain a positive integer (M).
#The second line of input will contain a positive integer (N).
#Output
#The output should be a single line containing the first perfect square in a given range.

m=int(input())
n=int(input())
row=[]
for j in range(m,n+1):
    for i in range(1,n+1):
        
        if i*i==j:
            row.append(j)
if len(row)>=1:
    print(row[0])
else:
    print("No Perfect Square")
        

        