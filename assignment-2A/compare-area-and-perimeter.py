#Write a program that reads the length and breadth of the rectangle and checks if the area of the rectangle is less than or equal to the perimeter of the rectangle.
length = int(input())
breadth = int(input())

area = (length * breadth)
perimeter = 2 * ( length + breadth)

result = (area <= perimeter)
print(result)