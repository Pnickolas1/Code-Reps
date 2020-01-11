

"""

Pascals Triangle

[   [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]

"""


def pascals_trianlge(numRows):
    pascal = [[1] * (i + 1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j -1] + pascal[i - 1][j]
    return pascal


print(pascals_trianlge(5))




def pascals_triangle_II(rowIndx):
    pascal = [1]* (rowIndx + 1)
    print(pascal)
    for i in range(2, rowIndx + 1):
        for j in range(i - 1, 0, -1):
            pascal[j] += pascal[j -1]
    return pascal

print(pascals_triangle_II(3))