#Given the number of sides, write a program to print the name of the polygon.
#If the given number of sides is less than 3, print "Not Polygon".
#If the given number of sides is equal to 3, print "Triangle".
#If the given number of sides is equal to 4, print "Quadrilateral". If the given number of sides is equal to 5, print "Pentagon". If the given number of sides is greater than 5, print "Big Polygon".
sides = int(input())

if sides < 3:
    print("Not Polygon")
elif sides == 3:
    print("Triangle")
elif sides == 4:
    print("Quadrilateral")
elif sides == 5:
    print("Pentagon")
elif sides > 5:
    print("Big Polygon")