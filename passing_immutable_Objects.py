def increment(a):   # This variable 'a' is refering different object
    a += 1
    print(a)

a = int(input())    # and This variable 'a' is refering different object, 
increment(a)    #Output:10
print(a)        #Output:9