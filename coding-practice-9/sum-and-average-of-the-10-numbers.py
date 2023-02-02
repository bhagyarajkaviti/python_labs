#Write a program to print the sum and average of the given ten numbers. 
#Average is the sum of the given numbers divided by the number of given numbers.
sum = 0
for i in range(1,11):
    numbers = int(input())
    sum += numbers
    Average = sum / i
    
print(sum)
print(Average)