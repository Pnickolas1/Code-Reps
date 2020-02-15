
"""

Zig Zag Traverse

given an array that takes in a two-dimensional array and retruns a one-dimensional array of all the array's
elements in zigzag order.

space: O(n)
time: O(n)

"""

def isOutOfBounds(row, col, width, height):
    return row < 0 or row > height or col < 0 or col > width

def zigzagTraverse(matrix):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1
    results = []
    row, col = 0, 0
    goingDown = True

    while not isOutOfBounds(row, col, width, height):
        results.append(matrix[row][col])
        if goingDown:
            if row == height or col == 0:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return results

sampleInput = [[1,3,4,10],
               [2,5,9,11],
               [6,8,12,15],
               [7,13,14,16]
               ]

testReturn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


print(zigzagTraverse(sampleInput))