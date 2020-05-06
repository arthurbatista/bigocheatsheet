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

print(one_away('pale', 'ple'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'pales'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))
print(one_away('apple', 'aple'))

