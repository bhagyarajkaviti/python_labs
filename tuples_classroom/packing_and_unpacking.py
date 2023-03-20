#Example 1: unpacking and packing
def get_sum_and_product(a, b):
    num_sum = a + b
    num_product = a * b
    return num_sum, num_product
result = get_sum_and_product(2, 3)
print(result)
x, y = get_sum_and_product(2, 3)
print(x)
print(y)
