for a in range(2):
    print("Outer: " + str(a))
    for b in range(4):
        if b == 1:
            break
        print(" inner: " + str(b))