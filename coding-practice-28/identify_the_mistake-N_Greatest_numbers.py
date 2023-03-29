#For this problem, the prefilled code will contain a list. Write a program to print N greatest numbers in a list.
list_a = [5, 20, 3, 7, 6, 8]
k = int(input())
list_a.sort()
list_len = len(list_a)
res = list_a[list_len - k:]
for i in range(k):
    res[i] = str(res[i])
    
print(" ".join(res))
