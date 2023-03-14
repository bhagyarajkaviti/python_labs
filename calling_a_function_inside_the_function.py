# Example 1: calling a function inside the function
def get_largest_sqr(list_x):
    len_list = len(list_x) #===> calling function len() inside the function get_largest_sqr()
    for i in range(len_list):
        x = list_x[i]
        list_x[i] = x * x 
    #print(list_x)      ===> [1, 9, 4]
    largest = max(list_x) #===>  calling function max() inside the function get_largest_sqr()
    return largest

list_a = [1, -3, 2]
result = get_largest_sqr(list_a)
print(result)

# Example 2: 
def get_sqrd_val(x):
    return (x * x)
def get_sum_of_sqrs(list_a):
    sqrs_sum = 0
    for i in list_a:
        sqrs_sum += get_sqrd_val(i) #===> calling a function `get_sqrd_val()` in another function `get_sum_of_sqrs()`
    return sqrs_sum

list_a = [1,2,3]
sum_of_sqrs = get_sum_of_sqrs(list_a)
print(sum_of_sqrs)