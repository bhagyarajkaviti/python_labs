#Sourav learnt the basic addition of two numbers which does not involve a carry. When he tries to add two numbers which involve a carry, he faces difficulty.
#Write a program that reads two numbers A and B and checks if Arjun faces difficulty or not.
#Input
#The input will be a single line contains two space-separated integers
#representing A and B.
#Output
#The output should be a single line containing a string. Hard should be printed if the addition of two numbers requires a carry,
#otherwise Easy should be printed.

n1,n2 = map(int,input().split())


if n1 > n2:
    large = str(n1)
    small = str(n2)
else:
    large = str(n2)
    small = str(n1)

add =n1 + n2
l1 = len(large)
l2 = len(small)
diff = l1 - l2
part_2 = str(add)[diff:]
l3 = len(part_2)
hard_found_count = 0
for i in range(1,l2+1):
    if int(large[-i]) + int(small[-i]) <= 9:
        hard_found_count += 1
        
    
if hard_found_count == l2:
    print("Easy")
else:
    print("Hard")