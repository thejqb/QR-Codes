import numpy as np

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
