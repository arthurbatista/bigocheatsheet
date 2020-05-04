def contains_unique(word):
    chars = [0 for i in range(0, 128)]
    for i in word:
        w = ord(i)
        if chars[w] == 1:
            return False
        chars[w] += 1
    return True

print(contains_unique('arthur'))
print(contains_unique('tolkien'))
