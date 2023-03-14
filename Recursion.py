#Recursion : Calling the same function inside the function itself is called recursion

#Example 1:
def multiply(n):    #===> Recursive function
    if n == 1: #===> this is `base case` or `base condition`
        return 1
    return n * multiply(n - 1)  #===> recursion takes place

num = int(input())  #Input:6
result = multiply(num)
print(result)       #Output:720