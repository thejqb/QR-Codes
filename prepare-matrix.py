import numpy as np

size = 21 + (version - 1) * 4
matrix = np.full((size, size), -1)

def place_finder_pattern(matrix, x, y):
    pattern = [
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]
    ]
    for i in range(7):
        for j in range(7):
            matrix[x+i][y+j] = pattern[i][j]
    return matrix

#Place finder patterns in three corners
matrix = place_finder_pattern(matrix, 0, 0)
matrix = place_finder_pattern(matrix, 0, size - 7)
matrix = place_finder_pattern(matrix, size - 7, 0)

#Place separators around the finder patterns
matrix[7, 0:8] = 0
matrix[0:8, 7] = 0
matrix[7, size-8:] = 0
matrix[0:8, size-8] = 0
matrix[size-8, 0:8] = 0
matrix[size-8:, 7] = 0

#Place timing patterns with alternating color
for i in range(8, size-8):
    matrix[6][i] = (i + 1) % 2 
    matrix[i][6] = (i + 1) % 2

#Dark module
matrix[size-8][8] = 1

#Reserve places for format information with -2
for i in range(9):
    if i != 6:
        matrix[8][i] = -2
        matrix[i][8] = -2
    if i != 8:
        matrix[8][size-1-i] = -2
        if i != 7:
            matrix[size-1-i][8] = -2

#Similarly reserve places for version info on versions 7+
if version >= 7:
    for i in range(6):
        for j in range(3):
            matrix[i][size-9-j] = -2
            matrix[size-9-j][i] = -2
            
def place_alignment_pattern(matrix, x, y):
    pattern = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]
    ]
    for i in range(5):
        for j in range(5):
            matrix[x-2+i][y-2+j] = pattern[i][j]
    return matrix

#List containing locations for alignment patterns
alignment_pattern_locations = [
    [],
    [6, 18],
    [6, 22],
    [6, 26],
    [6, 30],
    [6, 34],
    [6, 22, 38],
    [6, 24, 42],
    [6, 26, 46],
    [6, 28, 50],
    [6, 30, 54],
    [6, 32, 58],
    [6, 34, 62],
    [6, 26, 46, 66],
    [6, 26, 48, 70],
    [6, 26, 50, 74],
    [6, 30, 54, 78],
    [6, 30, 56, 82],
    [6, 30, 58, 86],
    [6, 34, 62, 90],
    [6, 28, 50, 72, 94],
    [6, 26, 50, 74, 98],
    [6, 30, 54, 78, 102],
    [6, 28, 54, 80, 106],
    [6, 32, 58, 84, 110],
    [6, 30, 58, 86, 114],
    [6, 34, 62, 90, 118],
    [6, 26, 50, 74, 98, 122],
    [6, 30, 54, 78, 102, 126],
    [6, 26, 52, 78, 104, 130],
    [6, 30, 56, 82, 108, 134],
    [6, 34, 60, 86, 112, 138],
    [6, 30, 58, 86, 114, 142],
    [6, 34, 62, 90, 118, 146],
    [6, 30, 54, 78, 102, 126, 150],
    [6, 24, 50, 76, 102, 128, 154],
    [6, 28, 54, 80, 106, 132, 158],
    [6, 32, 58, 84, 110, 136, 162],
    [6, 26, 54, 82, 110, 138, 166],
    [6, 30, 58, 86, 114, 142, 170]
]

positions = alignment_pattern_locations[version - 1]
for i in positions:
    for j in positions:
        if (i == 6 and (j == 6 or j == positions[-1])) or i == positions[-1] and j == 6:
            continue
        place_alignment_pattern(matrix, i, j)
