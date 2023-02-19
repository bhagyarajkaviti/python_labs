for a in range(3):
    if a == 1:
        continue
    print(a)
print("End")

#'continue' makes the program skip the remaining statements in the current iteration and begin the next iteration.

for b in range(3):
    continue
    print(b)
print("End")


#for c in range(3):
#    print(c)               #OUTPUT:
#continue                   #SyntaxError:
#print("end")               'continue' not properly in loop   