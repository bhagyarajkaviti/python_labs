#nested loop concept :
# AN inner loop within the repeating block of an outer loop is called nested loop.
    # the inner loop will be executed one time for each iteration of the outer loop.

for a in range(3):
    print("Outer: " + str(a))
    for b in range(7, 9):
        print(" inner: " + str(b)) 

print("End")