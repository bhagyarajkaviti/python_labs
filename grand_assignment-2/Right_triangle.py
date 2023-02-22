#Given a number N, write a program to print a triangular pattern of N lines with numbers as shown below.
#   1
#   121
#   12321
#   1234321
row = int(input())


for i in range(1, row + 1):
    forward = ""
    backward = ""
    for j in range(1 , i+1):
        forward = forward + str(j)
        
    for k in range(1, i):
        backward = str(k) + backward
    print(forward + backward)
    
# Another solution

#n = int(input())

#for i in range(1, n + 1):
#    pattern = ""
#    pattern1 = ""
#    for j in range(1, i + 1):
#        pattern = pattern + str(j) 
#        pattern1 = str(int(j-1)) + pattern1 
#        pattern1 = pattern1.replace(str(0), "")
#    print(pattern + pattern1)
        