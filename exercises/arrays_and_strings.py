# 1.1 - Is Unique
def contains_unique(word):
    chars = [0 for i in range(128)]
    for i in word:
        w = ord(i)
        if chars[w] == 1:
            return False
        chars[w] += 1
    return True

# print(contains_unique('arthur'))
# print(contains_unique('tolkien'))

# 1.2 Check Permutation
# given two string, check if one is a permutation of other
# another way to implement is sorting and comparing both strings
#   it is simple but not so efficient
def check_string_permutation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    if str_1 == str_2:
        return True
    
    chars = [0 for i in range(0, 128)]
    for i in str_1:
        w = ord(i)
        chars[w] += 1

    for i in str_2:
        w = ord(i)
        chars[w] -= 1
        if chars[w] < 0:
            return False

    return True

# print(check_string_permutation('arthur', 'ruhtra'))
# print(check_string_permutation('arthur', 'ruhtr'))

# 1.3 URLify
def urlfy(_str):
    result = ''
    for c in _str:
        if len(result) == len(_str):
            break
        if c == ' ':
            if result == '':
                continue
            if len(result) < 3 or result[:-3] != '%20':
                result += '%20'
        else:
            result += c
    return result

# print(urlfy('Mr John Smith    '))
# print(urlfy(' M r John Smith     '))

# 1.4 Palindrome
# Check if a given string contais a palindrome
def contains_palindrome(array):
    char_size = ord('z') - ord('a')
    index_table = [None for i in range(char_size)]
    hash_table = []

    def hash(c):
        return (ord(c) - ord('a'))

    # set char index 
    for c in array:
        if index_table[hash(c)] == None:
            idx = len(hash_table)
            index_table[hash(c)] = idx
            hash_table.append(1)
        else:
            hash_table[index_table[hash(c)]] += 1

    odds = 0
    for i in hash_table:
        if i % 2 != 0:
            odds += 1

        if odds > 1:
            return False

    return True

# print(contains_palindrome('arthur')) # False
# print(contains_palindrome('civic')) # True

# 1.5 One Away
def one_away(term_1, term_2):

    size_t1 = len(term_1)
    size_t2 = len(term_2)
    
    change = False
    i = j = 0
    while i < size_t1 and j < size_t2:
        if term_1[i] != term_2[j]:
            if size_t2 < size_t1:
                i += 1
            elif size_t2 > size_t1:
                j += 1

            if change:
                return False
            else:
                change = True
        i += 1
        j += 1

    return True

# print(one_away('pale', 'ple'))
# print(one_away('pales', 'pale'))
# print(one_away('pale', 'pales'))
# print(one_away('pale', 'bale'))
# print(one_away('pale', 'bake'))
# print(one_away('apple', 'aple'))


# 1.6 String Compression
def string_compression(_str):

    def __calc_compression_size(_str):
        size = count = 0

        for i in range(len(_str)):
            count += 1

            if i + 1 >= len(_str) or _str[i] != _str[i + 1]:
                size += 1 + len(str(count))
                count = 0

        return size

    size = __calc_compression_size(_str)
    if size >= len(_str):
        return _str

    result = [None for x in range(size)]
    result_pointer = 0
    count = 0

    for i in range(len(_str)):
        count += 1
        
        if i + 1 >= len(_str) or _str[i] != _str[i + 1]:
            result[result_pointer] = _str[i]
            result[result_pointer + 1] = str(count)
            count = 0
            result_pointer += 2

    return ''.join(result)

print(string_compression('arthur'))
print(string_compression('aaaaaaaarthur'))
print(string_compression('aaaabbbccd'))
# print(string_compression('aaaa'))

# 1.7 Rotate Matrix
# Rotate Matrix 90 degrees
# Do it by rotating from external layer to inner layer
def rotate_matrix():
    def rotate(matrix, new_matrix, layer):
        start = 0 + layer
        end = len(matrix) - 1 - layer
        for x in range(start, end + 1):
            new_matrix[x][end] = matrix[start][x]
            new_matrix[x][start] = matrix[end][x]
            new_matrix[end][end - x] = matrix[start + x][end]
            new_matrix[start][end - x] = matrix[start + x][start]

    matrix = [
        [1, 1, 1, 2],
        [4, 5, 5, 2],
        [4, 6, 6, 2],
        [4, 3, 3, 3]
    ]

    new_matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    for x in range(len(matrix) - 2):
        rotate(matrix, new_matrix, x)

    for l in new_matrix:
        print(l)

# rotate_matrix() 

# 1.8 Zero Matrix
# Given a matrix, set to Zero the rows and columns of
# a cell when it is Zero.
# The solution set the top cell and most left cell of a cell when it is Zero.
# After that, iterates over the firs row and fisrt colunm to find cells with Zero.
def set_row_column_to_zero():
    matrix = [
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]

    def zerofy_row(matrix, r):
        for i in range(len(matrix[r])):
            matrix[r][i] = 0

    def zerofy_column(matrix, c):
        for i in range(len(matrix)):
            matrix[i][c] = 0

    row_has_zero = col_has_zero = False

    for i in matrix[0]:
        if i == 0:
            row_has_zero = True

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col_has_zero = True

    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[x])):
            if matrix[x][y] == 0:
                matrix[0][y] = 0
                matrix[x][0] = 0

    for i in range(1, len(matrix[0])):
        if matrix[0][i] == 0:
            zerofy_column(matrix, i)

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            zerofy_row(matrix, i)

    if row_has_zero:
        zerofy_row(matrix, 0)

    if col_has_zero:
        zerofy_column(matrix, 0)

    for l in matrix:
        print(l)

# set_row_column_to_zero()