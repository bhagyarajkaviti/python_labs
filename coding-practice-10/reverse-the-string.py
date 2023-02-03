#write a program to print the reverse of the given string.
string = input()

j = len(string) - 1
k = ""
#while j >= 0:
#    k = k + string[j]
#    j -= 1

#print(k)
  
for i in string:
    k = i + k
    
print(k)