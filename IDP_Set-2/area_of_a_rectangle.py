#Given an MXN matrix filled with X 's and O's, find the largest rectangle containing only X's and return its area. If there are no Xs in the entire matrix print 0.
#Input
#The first line of input will be containing two space-separated integers, denoting M and N. The next M lines will contain N space-separated integers, denoting the elements of the matrix.
#Output
#The output should be a single line containing the area of the maximum rectangle.


def max_rectangle_area(matrix):
    # If the matrix is empty, there are no X's
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    left = [0] * n
    right = [n] * n
    max_area = 0

    for i in range(m):
        # Update the heights of each column
        for j in range(n):
            if matrix[i][j] == 'X':
                heights[j] += 1
            else:
                heights[j] = 0

        # Update the left boundary of each column
        cur_left = 0
        for j in range(n):
            if matrix[i][j] == 'X':
                left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1

        # Update the right boundary of each column
        cur_right = n
        for j in range(n-1, -1, -1):
            if matrix[i][j] == 'X':
                right[j] = min(right[j], cur_right)
            else:
                right[j] = n
                cur_right = j

        # Calculate the area of the largest rectangle containing only X's
        for j in range(n):
            area = heights[j] * (right[j] - left[j])
            max_area = max(max_area, area)

    return max_area


m,n = map(int, input().split())
matrix = []

for i in range(m):
    row = input().split()
    matrix.append(row)

max_area = max_rectangle_area(matrix)
print(max_area)