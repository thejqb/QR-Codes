import numpy as np
matrixcopy = matrix.copy()

row = size - 1
count = 0
col = size - 1
dir_up = True

while col > 0:
    if col == 6:
        col -= 1
    row_range = range(size - 1, -1, -1) if dir_up else range(size)
    for row in row_range:
        for c in [col, col - 1]:
            if matrix[row][c] == -1:
                if count < len(message_final):
                    matrix[row][c] = int(message_final[count])
                    count += 1
    dir_up = not dir_up
    col -= 2

matrix[matrix == -1] = 0

def domask(matrix, mask):
    size = matrix.shape[0]
    masked = matrix.copy()

    for i in range(size):
        for j in range(size):
            if matrix[i][j] not in (0, 1):
                continue

            apply = False
            if mask == 0:
                apply = (i + j) % 2 == 0
            elif mask == 1:
                apply = i % 2 == 0
            elif mask == 2:
                apply = j % 3 == 0
            elif mask == 3:
                apply = (i + j) % 3 == 0
            elif mask == 4:
                apply = (i // 2 + j // 3) % 2 == 0
            elif mask == 5:
                apply = ((i * j) % 2 + (i * j) % 3) == 0
            elif mask == 6:
                apply = (((i * j) % 2 + (i * j) % 3) % 2) == 0
            elif mask == 7:
                apply = (((i + j) % 2 + (i * j) % 3) % 2) == 0

            if apply:
                masked[i][j] ^= 1

    return masked

def penalty(matrix):
    size = matrix.shape[0]
    total = 0

    for axis in [0, 1]:
        for i in range(size):
            line = matrix[i, :] if axis == 0 else matrix[:, i]
            run_color = line[0]
            run_length = 1
            for j in range(1, size):
                if line[j] == run_color:
                    run_length += 1
                else:
                    if run_length >= 5:
                        total += 3 + (run_length - 5)
                    run_color = line[j]
                    run_length = 1
            if run_length >= 5:
                total += 3 + (run_length - 5)

    for i in range(size - 1):
        for j in range(size - 1):
            block = matrix[i:i+2, j:j+2]
            if np.all(block == block[0, 0]):
                total += 3

    pattern1 = [1, 0, 1, 1, 1, 0, 1]
    pattern2 = [0, 0, 0, 0]
    for i in range(size):
        for j in range(size - 10):
            row = matrix[i, j:j+11]
            col = matrix[j:j+11, i]
            if list(row[:7]) == pattern1 and (list(row[7:11]) == pattern2 or list(row[0:4]) == pattern2):
                total += 40
            if list(col[:7]) == pattern1 and (list(col[7:11]) == pattern2 or list(col[0:4]) == pattern2):
                total += 40

    num_dark = np.sum(matrix == 1)
    num_total = np.sum(np.isin(matrix, [0, 1]))
    ratio = 100 * num_dark / num_total
    prev_multiple = int(ratio // 5) * 5
    next_multiple = prev_multiple + 5
    total += min(abs(prev_multiple - 50), abs(next_multiple - 50)) // 5 * 10

    return total

best_score = float('inf')
best_mask = None
best_matrix = None

for mask in range(8):
    candidate = domask(matrix, mask)
    score = penalty(candidate)
    if score < best_score:
        best_score = score
        best_mask = mask
        best_matrix = candidate
        print(mask)

matrix = domask(matrix, best_mask)

for i in range(size):
    for j in range(size):
        if matrixcopy[i][j] != -1:
            matrix[i][j] = matrixcopy[i][j]
