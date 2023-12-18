import time


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def addition(poly_1, poly_2):
    poly_1 = poly_1.zfill(173)
    poly_2 = poly_2.zfill(173)
    c = ['0']
    for i in range(173):
        c.append(str(((int(poly_1[i]) if i < len(poly_1) else 0) ^ (int(poly_2[i]) if i < len(poly_2) else 0))))
    result = ''.join(c)
    return result.lstrip('0') if len(result) <= 173 else result[(len(result) - 173):]


def matrix_create():
    p = 2 * 173 + 1
    multiplicative_matrix = [[0] * 173 for _ in range(173)]
    for i in range(173):
        for j in range(173):
            if (2 ** i + 2 ** j) % p == 1:
                multiplicative_matrix[i][j] = 1
            elif (2 ** i - 2 ** j) % p == 1:
                multiplicative_matrix[i][j] = 1
            elif (-1 * 2 ** i + 2 ** j) % p == 1:
                multiplicative_matrix[i][j] = 1
            elif (-1 * 2 ** i - 2 ** j) % p == 1:
                multiplicative_matrix[i][j] = 1
            else:
                multiplicative_matrix[i][j] = 0
    return multiplicative_matrix


def left_shift(number, shift):
    num_list = list(number)
    num_list = num_list[shift:] + num_list[:shift]
    result = ''
    for i in num_list:
        result += i
    return result


def mul(a, b):
    result = ''
    multiplicative_matrix = matrix_create()

    a = a.zfill(173)
    b = b.zfill(173)

    for z in range(173):
        result_1 = [0 for _ in range(173)]
        result_2 = 0
        pre_1 = left_shift(a, z)
        pre_2 = left_shift(b, z)

        for i in range(173):
            for j in range(173):
                result_1[i] += int(pre_1[j]) * multiplicative_matrix[j][i]
            result_1[i] = result_1[i] % 2

        for i in range(173):
            result_2 += result_1[i] * int(pre_2[i])
        result_2 = result_2 % 2
        result += str(result_2)

    return result


def square(bitstring):
    shift = 1
    length = len(bitstring)
    shift %= length
    shifted_bits = bitstring[-shift:] + bitstring[:-shift]
    return shifted_bits


def power(poly_1, poly_3):
    result = '1'
    binary_exponent = ''.join(map(str, poly_3))
    current_power = poly_1
    for bit in binary_exponent[::-1]:
        if bit == '1':
            result = mul(result, current_power)
        current_power = square(current_power)
    return result


def reverse(poly_1):
    power_reverse = 2 ** 173 - 2
    power_reverse = bin(power_reverse)[2:]
    power_reverse = str(power_reverse)
    return power(poly_1, power_reverse)


def trace(poly):
    result = 0
    for char in poly:
        result += int(char)
    return result % 2


poly1_str = "11010111011111010010001010110111000111100110001011100000011011110101011000001100100011000101110001111011110011010010001111111101010001011001001100011011011111111011111110110"
poly2_str = "10100100011101101100101001110110101010111011001101110000111101001011110001000111000001110000001110000000000111100010010111100110101101011000111000000011111100111111100111011"
poly3_str = '10000110110100011101010101100100110101100010001111110010010011100001000111001011111101000001100011000101011101111011011001000111011111001001001000110001101000101111001011110'


add_result, add_time = measure_time(addition, poly1_str, poly2_str)
print(f'Addition:  {add_result}')
print(f'Time taken for Addition: {add_time} seconds')

mul_result, mul_time = measure_time(mul, poly1_str, poly2_str)
print(f'Multiply:  {mul_result}')
print(f'Time taken for Multiply: {mul_time} seconds')

sq_result, sq_time = measure_time(square, poly1_str)
print(f'Square:  {sq_result}')
print(f'Time taken for Square: {sq_time} seconds')

reverse_result, reverse_time = measure_time(reverse, poly1_str)
print(f'Reverse:  {reverse_result}')
print(f'Time taken for Reverse: {reverse_time} seconds')

pow_result, pow_time = measure_time(power, poly1_str, poly3_str)
print(f'Power:  {pow_result}')
print(f'Time taken for Power: {pow_time} seconds')

