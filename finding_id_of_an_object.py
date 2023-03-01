#example 1:
a = "Hello"
print(id(a))        #output:2557253800048
a = a + " World"
print(id(a))        #output:2557253433072

#example 2:
list_a = [1, 2, 3]
print(id(list_a[0]))    #output:140718364226344
print(id(list_a[1]))    #output:140718364226376
print(id(list_a[2]))    #output:140718364226408
print(id(list_a))       #output:2557253800768


  



