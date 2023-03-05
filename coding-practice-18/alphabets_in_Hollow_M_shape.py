#Given a number N, write a program to print the letter M of N rows using alphabets.
#    A         A
#   B B       B B
#  C   C     C   C
# D     D   D     D
#E       E E       E
n = int(input())
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    side_spaces = " " * (n- i - 1)
    center_space = " " * (n- i - 1) * 2
    hallow_sapce = " " * (2*i - 1)
    alphabet = alphabets[i]
    if i == 0:
        print(side_spaces + alphabet + center_space  + " " + alphabet)
    else:
        print(side_spaces + alphabet + hallow_sapce + alphabet + " " + center_space + alphabet + hallow_sapce + alphabet)
        
#Another solution for the same question


#n =int(input())
#for i in range(1,n+1):
#    a = chr(64+i)
#    if i ==1:
#        print(" "*(n-i)+a+" "*(n-i)+" "+" "*(n-i)+a+" "*(n-i))
#    else:
#        print(" "*(n-i)+a+" "*(2*(i-1)-1)+a+" "*(n-i)+" "+" "*(n-i)+a+" "*(2*(i-1)-1)+a+" "*(n-i))