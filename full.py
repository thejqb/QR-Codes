import numpy as np

data_lengths = {
    1:  {'L': 19,  'M': 16,  'Q': 13,  'H': 9},
    2:  {'L': 34,  'M': 28,  'Q': 22,  'H': 16},
    3:  {'L': 55,  'M': 44,  'Q': 34,  'H': 26},
    4:  {'L': 80,  'M': 64,  'Q': 48,  'H': 36},
    5:  {'L': 108, 'M': 86,  'Q': 62,  'H': 46},
    6:  {'L': 136, 'M': 108, 'Q': 76,  'H': 60},
    7:  {'L': 156, 'M': 124, 'Q': 88,  'H': 66},
    8:  {'L': 194, 'M': 154, 'Q': 110, 'H': 86},
    9:  {'L': 232, 'M': 182, 'Q': 132, 'H': 100},
    10: {'L': 274, 'M': 216, 'Q': 154, 'H': 122},
    11: {'L': 324, 'M': 254, 'Q': 180, 'H': 140},
    12: {'L': 370, 'M': 290, 'Q': 206, 'H': 158},
    13: {'L': 428, 'M': 334, 'Q': 244, 'H': 180},
    14: {'L': 461, 'M': 365, 'Q': 261, 'H': 197},
    15: {'L': 523, 'M': 415, 'Q': 295, 'H': 223},
    16: {'L': 589, 'M': 453, 'Q': 325, 'H': 253},
    17: {'L': 647, 'M': 507, 'Q': 367, 'H': 283},
    18: {'L': 721, 'M': 563, 'Q': 397, 'H': 313},
    19: {'L': 795, 'M': 627, 'Q': 445, 'H': 341},
    20: {'L': 861, 'M': 669, 'Q': 485, 'H': 385},
    21: {'L': 932, 'M': 714, 'Q': 512, 'H': 406},
    22: {'L': 1006, 'M': 782, 'Q': 568, 'H': 442},
    23: {'L': 1094, 'M': 860, 'Q': 614, 'H': 464},
    24: {'L': 1174, 'M': 914, 'Q': 664, 'H': 514},
    25: {'L': 1276, 'M': 1000, 'Q': 718, 'H': 538},
    26: {'L': 1370, 'M': 1062, 'Q': 754, 'H': 596},
    27: {'L': 1468, 'M': 1128, 'Q': 808, 'H': 628},
    28: {'L': 1531, 'M': 1193, 'Q': 871, 'H': 661},
    29: {'L': 1631, 'M': 1267, 'Q': 911, 'H': 701},
    30: {'L': 1735, 'M': 1373, 'Q': 985, 'H': 745},
    31: {'L': 1843, 'M': 1455, 'Q': 1033, 'H': 793},
    32: {'L': 1955, 'M': 1541, 'Q': 1115, 'H': 845},
    33: {'L': 2071, 'M': 1631, 'Q': 1171, 'H': 901},
    34: {'L': 2191, 'M': 1725, 'Q': 1231, 'H': 961},
    35: {'L': 2306, 'M': 1812, 'Q': 1286, 'H': 986},
    36: {'L': 2434, 'M': 1914, 'Q': 1354, 'H': 1054},
    37: {'L': 2566, 'M': 1992, 'Q': 1426, 'H': 1096},
    38: {'L': 2702, 'M': 2102, 'Q': 1502, 'H': 1142},
    39: {'L': 2812, 'M': 2216, 'Q': 1582, 'H': 1222},
    40: {'L': 2956, 'M': 2334, 'Q': 1666, 'H': 1276},
}

ec_lengths = {
    1:  {'L': 7,   'M': 10,  'Q': 13,  'H': 17},
    2:  {'L': 10,  'M': 16,  'Q': 22,  'H': 28},
    3:  {'L': 15,  'M': 26,  'Q': 36,  'H': 44},
    4:  {'L': 20,  'M': 36,  'Q': 52,  'H': 64},
    5:  {'L': 26,  'M': 48,  'Q': 72,  'H': 88},
    6:  {'L': 36,  'M': 64,  'Q': 96,  'H': 112},
    7:  {'L': 40,  'M': 72,  'Q': 108, 'H': 130},
    8:  {'L': 48,  'M': 88,  'Q': 132, 'H': 156},
    9:  {'L': 60,  'M': 110, 'Q': 160, 'H': 192},
    10: {'L': 72,  'M': 130, 'Q': 192, 'H': 224},
    11: {'L': 80,  'M': 150, 'Q': 224, 'H': 264},
    12: {'L': 96,  'M': 176, 'Q': 260, 'H': 308},
    13: {'L': 104, 'M': 198, 'Q': 288, 'H': 352},
    14: {'L': 120, 'M': 216, 'Q': 320, 'H': 384},
    15: {'L': 132, 'M': 240, 'Q': 360, 'H': 432},
    16: {'L': 144, 'M': 280, 'Q': 408, 'H': 480},
    17: {'L': 168, 'M': 308, 'Q': 448, 'H': 532},
    18: {'L': 180, 'M': 338, 'Q': 504, 'H': 588},
    19: {'L': 196, 'M': 364, 'Q': 546, 'H': 650},
    20: {'L': 224, 'M': 416, 'Q': 600, 'H': 700},
    21: {'L': 224, 'M': 442, 'Q': 644, 'H': 750},
    22: {'L': 252, 'M': 476, 'Q': 690, 'H': 816},
    23: {'L': 270, 'M': 504, 'Q': 750, 'H': 900},
    24: {'L': 300, 'M': 560, 'Q': 810, 'H': 960},
    25: {'L': 312, 'M': 588, 'Q': 870, 'H': 1050},
    26: {'L': 336, 'M': 644, 'Q': 952, 'H': 1110},
    27: {'L': 360, 'M': 700, 'Q': 1020, 'H': 1200},
    28: {'L': 390, 'M': 728, 'Q': 1050, 'H': 1260},
    29: {'L': 420, 'M': 784, 'Q': 1140, 'H': 1350},
    30: {'L': 450, 'M': 812, 'Q': 1200, 'H': 1440},
    31: {'L': 480, 'M': 868, 'Q': 1290, 'H': 1530},
    32: {'L': 510, 'M': 924, 'Q': 1350, 'H': 1620},
    33: {'L': 540, 'M': 980, 'Q': 1440, 'H': 1710},
    34: {'L': 570, 'M': 1036,'Q': 1530, 'H': 1800},
    35: {'L': 570, 'M': 1064,'Q': 1590, 'H': 1890},
    36: {'L': 600, 'M': 1120,'Q': 1680, 'H': 1980},
    37: {'L': 630, 'M': 1204,'Q': 1770, 'H': 2100},
    38: {'L': 660, 'M': 1260,'Q': 1860, 'H': 2220},
    39: {'L': 720, 'M': 1316,'Q': 1950, 'H': 2310},
    40: {'L': 750, 'M': 1372,'Q': 2040, 'H': 2430},
}

message = input("Message: ")
version = int(input("Version: "))
level = input("Error Correction Level:")
level = level.upper()
ec_length = ec_lengths[version][level]
data_length = data_lengths[version][level]

def conversion(message, version, level):
    count_bits = f'{len(message):08b}'
    data_bits = ''.join(f'{b:08b}' for b in message.encode('utf-8'))
    bitstream = '0100' + count_bits + data_bits
    remaining = data_length * 8 - len(bitstream)
    if remaining > 0:
        bitstream += '0' * min(4, remaining)
    while len(bitstream) % 8 != 0:
        bitstream += '0'
    codewords = [int(bitstream[i:i+8], 2) for i in range(0, len(bitstream), 8)]
    pad_bytes = [0xEC, 0x11]
    i = 0
    while len(codewords) < data_length:
        codewords.append(pad_bytes[i % 2])
        i += 1
    if len(bitstream) > data_length * 8:
        raise ValueError("Message too long")
    return codewords

ec_length = ec_lengths[version][level]
data_length = data_lengths[version][level]

converted = conversion(message, version, level)

poly = 0x11D
fieldsize = 256

exp = [0] * (2 * fieldsize)
log = [0] * fieldsize

def gentables():
    x = 1
    for i in range(fieldsize - 1):
        exp[i] = x
        log[x] = i
        x <<= 1
        if x & 0x100:
            x ^= poly
    for i in range(fieldsize - 1, 2 * fieldsize):
        exp[i] = exp[i - (fieldsize - 1)]

gentables()

def mult(x, y):
    if x == 0 or y == 0:
        return 0
    return exp[log[x] + log[y]]

def polymult(p, q):
    result = [0] * (len(p) + len(q) - 1)
    for i in range(len(p)):
        for j in range(len(q)):
            result[i + j] ^= mult(p[i], q[j])
    return result

def polydiv(p, q):
    p = list(p)
    q = list(q)
    result = list(p)
    deg = len(q) - 1
    lead = q[0]

    for i in range(len(p) - len(q) + 1):
        coef = result[i]
        if coef != 0:
            factor = log[coef] - log[lead]
            for j in range(len(q)):
                if q[j] != 0:
                    result[i + j] ^= exp[(log[q[j]] + factor)]

    remainder = result[-(len(q) - 1):]
    return remainder

def generator(ec_length):
    gen = [1]
    for i in range(ec_length):
        gen = polymult(gen, [1, exp[i]])  # (x - α^i)
    return gen

gen_poly = generator(ec_length)
remainder = polydiv(converted + [0] * (len(gen_poly) - 1), gen_poly)
message_bytes = converted + remainder
message_final = [int(bit) for byte in message_bytes for bit in f'{byte:08b}']

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
matrix[4 * version + 9][8] = 1

#Reserve places for format information with -2
for i in range(9):
    if i != 6:
        matrix[8][i] = -2
        matrix[i][8] = -2
        matrix[8][size-1-i] = -2
        matrix[size-1-i][8] = -2

#
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

#List containing locations for alignment patterns based on 
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
        if matrix[i][j] == -1:
            place_alignment_pattern(matrix, i, j)

matrixcopy = matrix

row = size - 1
bitstring = ''.join(f'{byte:08b}' for byte in message_final)
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
                if count < len(bitstring):
                    matrix[row][c] = int(bitstring[count])
                    count += 1
                else:
                    matrix[row][c] = 0
    dir_up = not dir_up
    col -= 2
    
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

matrix = domask(matrix, best_mask)

for i in range(size):
    for j in range(size):
        if matrixcopy[i][j] != -1:
            matrix[i][j] = matrixcopy[i][j]

def bch_format_string(format_info):
    g = 0b10100110111
    data = format_info << 10
    for i in range(14, 4, -1):
        if data & (1 << (i - 1)):
            data ^= g << (i - 5)
    return (format_info << 10 | data) ^ 0b101010000010010

def bch_version_info(version):
    g = 0b1111100100101
    data = version << 12
    for i in range(17, 11, -1):
        if data & (1 << (i - 1)):
            data ^= g << (i - 13)
    return version << 12 | data

def place_format_info(matrix, ec_level, mask_pattern):
    ec_dict = {'L': 1, 'M': 0, 'Q': 3, 'H': 2}
    ec_bits = ec_dict[ec_level] << 3 | mask_pattern
    fmt = bch_format_string(ec_bits)
    fmt_bits = f'{fmt:015b}'

    size = matrix.shape[0]

    for i in range(6):
        matrix[8][i] = int(fmt_bits[i])
    matrix[8][7] = int(fmt_bits[6])
    matrix[8][8] = int(fmt_bits[7])
    matrix[7][8] = int(fmt_bits[8])
    for i in range(6):
        matrix[5 - i][8] = int(fmt_bits[9 + i])

    for i in range(8):
        matrix[size - 1 - i][8] = int(fmt_bits[i])
    for i in range(7):
        matrix[8][size - 1 - i] = int(fmt_bits[8 + i])

    return matrix

def place_version_info(matrix, version):
    if version < 7:
        return matrix

    bits = f'{bch_version_info(version):018b}'
    size = matrix.shape[0]
    for i in range(6):
        for j in range(3):
            matrix[size - 11 + j][i] = int(bits[i * 3 + j])
            matrix[i][size - 11 + j] = int(bits[i * 3 + j])
    return matrix

matrix = place_format_info(matrix, level, best_mask)
matrix = place_version_info(matrix, version)

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.imshow(matrix, cmap='gray_r', interpolation='nearest')
plt.axis('off')
plt.title('QR Code')
plt.show()