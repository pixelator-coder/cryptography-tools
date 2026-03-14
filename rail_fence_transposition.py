import math

def get_transposed_string(original_string):
    first_half = ""
    second_half = ""
    for even_index in range(0, len(original_string), 2):
        first_half += original_string[even_index]
    for odd_index in range(1, len(original_string), 2):
        second_half += original_string[odd_index]
    transposed_string = first_half + second_half
    return transposed_string

def get_original_string(transposed_string):
    original_string = ""
    is_even = len(transposed_string) % 2 == 0
    half_length = math.floor((1/2)*(len(transposed_string)))
    if is_even:
        offset = half_length
    else:
        offset = half_length + 1
    for index in range(0, half_length, 1):
        original_string += transposed_string[index]
        original_string += transposed_string[index + offset]
    if not is_even:
        original_string += transposed_string[half_length]
    return original_string