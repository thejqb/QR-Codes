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

qr_blocks = {
    (1, 'L'):  ([1, 0], [19, 0], 7),    (1, 'M'):  ([1, 0], [16, 0], 10), (1, 'Q'):  ([1, 0], [13, 0], 13),   (1, 'H'):  ([1, 0], [9, 0], 17),
    (2, 'L'):  ([1, 0], [34, 0], 10),   (2, 'M'):  ([1, 0], [28, 0], 16), (2, 'Q'):  ([1, 0], [22, 0], 22),   (2, 'H'):  ([1, 0], [16, 0], 28),
    (3, 'L'):  ([1, 0], [55, 0], 15),   (3, 'M'):  ([1, 1], [28, 28], 26), (3, 'Q'):  ([2, 0], [17, 0], 18),   (3, 'H'):  ([2, 0], [13, 0], 22),
    (4, 'L'):  ([1, 0], [80, 0], 20),   (4, 'M'):  ([2, 0], [32, 0], 18), (4, 'Q'):  ([2, 0], [24, 0], 26),   (4, 'H'):  ([4, 0], [9, 0], 16),
    (5, 'L'):  ([1, 0], [108, 0], 26),  (5, 'M'):  ([2, 0], [43, 0], 24), (5, 'Q'):  ([2, 2], [15, 16], 18),  (5, 'H'):  ([2, 2], [11, 12], 22),
    (6, 'L'):  ([2, 0], [68, 0], 18),   (6, 'M'):  ([4, 0], [27, 0], 16), (6, 'Q'):  ([4, 0], [19, 0], 24),   (6, 'H'):  ([4, 0], [15, 0], 28),
    (7, 'L'):  ([2, 0], [78, 0], 20),   (7, 'M'):  ([4, 0], [31, 0], 18), (7, 'Q'):  ([2, 4], [14, 15], 18),  (7, 'H'):  ([4, 1], [13, 14], 26),
    (8, 'L'):  ([2, 0], [97, 0], 24),   (8, 'M'):  ([2, 2], [38, 39], 22), (8, 'Q'):  ([4, 2], [18, 19], 22),  (8, 'H'):  ([4, 2], [14, 15], 26),
    (9, 'L'):  ([2, 0], [116, 0], 30),  (9, 'M'):  ([3, 2], [36, 37], 22), (9, 'Q'):  ([4, 4], [16, 17], 20),  (9, 'H'):  ([4, 4], [12, 13], 24),
    (10, 'L'): ([2, 2], [68, 69], 28),  (10, 'M'): ([4, 1], [43, 44], 26), (10, 'Q'): ([6, 2], [19, 20], 24),  (10, 'H'): ([6, 2], [15, 16], 28),
    (11, 'L'): ([4, 0], [58, 0], 30), (11, 'M'): ([1, 4], [50, 51], 28), (11, 'Q'): ([4, 4], [22, 23], 24), (11, 'H'): ([3, 8], [12, 13], 20),
    (12, 'L'): ([2, 2], [69, 70], 22), (12, 'M'): ([6, 2], [42, 43], 26), (12, 'Q'): ([4, 6], [24, 25], 28), (12, 'H'): ([7, 4], [12, 13], 24),
    (13, 'L'): ([4, 0], [80, 0], 22), (13, 'M'): ([8, 1], [36, 37], 24), (13, 'Q'): ([8, 4], [20, 21], 22), (13, 'H'): ([12, 4], [11, 12], 22),
    (14, 'L'): ([3, 1], [95, 96], 24), (14, 'M'): ([4, 5], [44, 45], 28), (14, 'Q'): ([11, 5], [16, 17], 24), (14, 'H'): ([11, 5], [12, 13], 24),
    (15, 'L'): ([5, 1], [96, 97], 24), (15, 'M'): ([5, 5], [44, 45], 28), (15, 'Q'): ([5, 7], [24, 25], 24), (15, 'H'): ([11, 7], [12, 13], 24),
    (16, 'L'): ([5, 1], [108, 109], 28), (16, 'M'): ([7, 3], [44, 45], 28), (16, 'Q'): ([15, 2], [19, 20], 30), (16, 'H'): ([3, 13], [15, 16], 30),
    (17, 'L'): ([1, 5], [112, 113], 28), (17, 'M'): ([10, 1], [46, 47], 28), (17, 'Q'): ([1, 15], [22, 23], 28), (17, 'H'): ([2, 17], [14, 15], 28),
    (18, 'L'): ([5, 1], [116, 117], 28), (18, 'M'): ([9, 4], [46, 47], 28), (18, 'Q'): ([17, 1], [22, 23], 28), (18, 'H'): ([2, 19], [14, 15], 28),
    (19, 'L'): ([3, 4], [117, 118], 28), (19, 'M'): ([3, 11], [47, 48], 28), (19, 'Q'): ([17, 4], [21, 22], 28), (19, 'H'): ([9, 16], [13, 14], 28),
    (20, 'L'): ([3, 5], [118, 119], 28), (20, 'M'): ([3, 13], [45, 46], 28), (20, 'Q'): ([15, 5], [24, 25], 28), (20, 'H'): ([15, 10], [15, 16], 28),
    (21, 'L'): ([4, 4], [121, 122], 28), (21, 'M'): ([17, 0], [46, 0], 28), (21, 'Q'): ([17, 6], [22, 23], 30), (21, 'H'): ([19, 6], [16, 17], 30),
    (22, 'L'): ([2, 7], [117, 118], 28), (22, 'M'): ([17, 0], [47, 0], 28), (22, 'Q'): ([7, 16], [24, 25], 30), (22, 'H'): ([34, 0], [13, 0], 24),
    (23, 'L'): ([4, 5], [122, 123], 30), (23, 'M'): ([4, 14], [46, 47], 30), (23, 'Q'): ([11, 14], [24, 25], 30), (23, 'H'): ([16, 14], [15, 16], 30),
    (24, 'L'): ([6, 4], [122, 123], 30), (24, 'M'): ([6, 14], [47, 48], 30), (24, 'Q'): ([11, 16], [24, 25], 30), (24, 'H'): ([30, 2], [16, 17], 30),
    (25, 'L'): ([8, 4], [122, 123], 26), (25, 'M'): ([8, 13], [47, 48], 30), (25, 'Q'): ([7, 22], [24, 25], 30), (25, 'H'): ([22, 13], [15, 16], 30),
    (26, 'L'): ([10, 2], [122, 123], 28), (26, 'M'): ([19, 4], [46, 47], 28), (26, 'Q'): ([28, 6], [22, 23], 28), (26, 'H'): ([33, 4], [16, 17], 28),
    (27, 'L'): ([8, 4], [122, 123], 30), (27, 'M'): ([22, 3], [45, 46], 30), (27, 'Q'): ([8, 26], [23, 24], 30), (27, 'H'): ([12, 28], [15, 16], 30),
    (28, 'L'): ([3, 10], [122, 123], 30), (28, 'M'): ([3, 23], [45, 46], 30), (28, 'Q'): ([4, 31], [24, 25], 30), (28, 'H'): ([11, 31], [15, 16], 30),
    (29, 'L'): ([7, 7], [122, 123], 30), (29, 'M'): ([21, 7], [45, 46], 30), (29, 'Q'): ([1, 37], [23, 24], 30), (29, 'H'): ([19, 26], [15, 16], 30),
    (30, 'L'): ([5, 10], [122, 123], 30), (30, 'M'): ([19, 10], [45, 46], 30), (30, 'Q'): ([15, 25], [24, 25], 30), (30, 'H'): ([23, 25], [15, 16], 30),
    (31, 'L'): ([13, 3], [122, 123], 30), (31, 'M'): ([2, 29], [45, 46], 30), (31, 'Q'): ([42, 1], [24, 25], 30), (31, 'H'): ([23, 28], [15, 16], 30),
    (32, 'L'): ([17, 0], [122, 0], 30), (32, 'M'): ([10, 23], [45, 46], 30), (32, 'Q'): ([10, 35], [24, 25], 30), (32, 'H'): ([19, 35], [15, 16], 30),
    (33, 'L'): ([17, 1], [122, 123], 30), (33, 'M'): ([14, 21], [45, 46], 30), (33, 'Q'): ([29, 19], [24, 25], 30), (33, 'H'): ([11, 46], [15, 16], 30),
    (34, 'L'): ([13, 6], [122, 123], 30), (34, 'M'): ([14, 23], [45, 46], 30), (34, 'Q'): ([44, 7], [24, 25], 30), (34, 'H'): ([59, 1], [15, 16], 30),
    (35, 'L'): ([12, 7], [122, 123], 30), (35, 'M'): ([12, 26], [45, 46], 30), (35, 'Q'): ([39, 14], [24, 25], 30), (35, 'H'): ([22, 41], [15, 16], 30),
    (36, 'L'): ([6, 14], [122, 123], 30), (36, 'M'): ([6, 34], [45, 46], 30), (36, 'Q'): ([46, 10], [24, 25], 30), (36, 'H'): ([2, 64], [15, 16], 30),
    (37, 'L'): ([17, 4], [122, 123], 30), (37, 'M'): ([29, 14], [45, 46], 30), (37, 'Q'): ([49, 10], [24, 25], 30), (37, 'H'): ([24, 46], [15, 16], 30),
    (38, 'L'): ([4, 18], [122, 123], 30), (38, 'M'): ([13, 32], [45, 46], 30), (38, 'Q'): ([48, 14], [24, 25], 30), (38, 'H'): ([42, 32], [15, 16], 30),
    (39, 'L'): ([20, 4], [122, 123], 30), (39, 'M'): ([40, 7], [45, 46], 30), (39, 'Q'): ([43, 22], [24, 25], 30), (39, 'H'): ([10, 67], [15, 16], 30),
    (40, 'L'): ([19, 6], [122, 123], 30), (40, 'M'): ([18, 31], [45, 46], 30), (40, 'Q'): ([34, 34], [24, 25], 30), (40, 'H'): ([20, 61], [15, 16], 30)
}


key = (version, level)

group_counts, group_sizes, ecc_len = qr_blocks[key]
total_blocks = sum(group_counts)
data_blocks = []
ecc_blocks = []

i = 0
for group_id in range(2):
    for _ in range(group_counts[group_id]):
        size = group_sizes[group_id]
        block = converted[i:i+size]
        i += size
        data_blocks.append(block)
        ecc = polydiv(block + [0]*ecc_len, generator(ecc_len))
        ecc_blocks.append(ecc)

interleaved = []

max_data_len = max(len(b) for b in data_blocks)
for i in range(max_data_len):
    for block in data_blocks:
        if i < len(block):
            interleaved.append(block[i])

for i in range(ecc_len):
    for block in ecc_blocks:
        interleaved.append(block[i])

message_bytes = interleaved
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
    
def bch_format_string(format_info):
    g = 0b10100110111
    data = format_info << 10
    for i in range(data.bit_length() - 1, 9, -1):
        if data & (1 << i):
            data ^= g << (i - 10)
    return (format_info << 10 | data) ^ 0b101010000010010

def bch_version_info(version):
    g = 0b1111100100101 
    data = version << 12
    for i in range(data.bit_length() - 1, 11, -1):
        if data & (1 << i):
            data ^= g << (i - 12)
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

    for i in range(7):
        matrix[size - 1 - i][8] = int(fmt_bits[i])
    for i in range(8):
        matrix[8][size - 1 - i] = int(fmt_bits[7 + i])

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
plt.show(block=False)   
plt.pause(6)       
plt.close()
