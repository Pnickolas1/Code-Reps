

"""

Pascals Triangle

[   [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]

"""

# 118
def pascalsTriangle(num_rows):
    triangle = []

    for row_num in range(num_rows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num + 1)]
        row[0], row[-1] = 1, 1
        print(row)
        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row) - 1):
            print(row)
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle

print(pascalsTriangle(5))



def pascals_triangle_II(rowIndx):
    pascal = [1]* (rowIndx + 1)
    print(pascal)
    for i in range(2, rowIndx + 1):
        for j in range(i - 1, 0, -1):
            pascal[j] += pascal[j -1]
    return pascal

print(pascals_triangle_II(3))