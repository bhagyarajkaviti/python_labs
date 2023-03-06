# Negative Indexing: starts with 1st item as index(-n) and ends last item as index(-1)
# Indexing(positice) : starts with 1st item as index(0) and ends last item as index(n-1) 
list_a = [5, 4, 3, 2, 1]
item = list_a[-4]
print(item)

# Example 2:
list_a = [45,29,67,21,54]
list_b = list_a[-4:-1]
list_c = list_a[-9:-1]
print(list_b)       #Output : [29, 67, 21]
print(list_c)       #Output : [45, 29, 67, 21]


#Extended slicing(Negative Slicing)
#Example 3:
list_a = [45,29,67,21,54]
list_b = list_a[4:2:-1]
print(list_b)       #Output : [54, 21]