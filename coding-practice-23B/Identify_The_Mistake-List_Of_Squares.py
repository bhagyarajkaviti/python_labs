#Given a list of integers, write a program to square the elements in the given list.
def get_list(string_a):
    list_a = string_a.split(',')
    len_list_a = len(list_a)
    for i in range(len_list_a):
        list_a[i] = int(list_a[i]) ** 2
    return list_a


string_a = input()
numbers_list = get_list(string_a)
print(numbers_list)
