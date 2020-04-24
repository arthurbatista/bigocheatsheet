def merge(left, right):
    result = []

    while(left and right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left

    if right:
        result += right

    return result

def msort(_list):

    if len(_list) == 1:
        return _list

    i = int(len(_list)) / 2

    left = _list[:i]
    right = _list[i:]

    return merge(msort(left), msort(right))


print(msort([5, 4, 3, 2, 1]))
print(msort([1, 2, 3, 4, 5]))
print(msort([3, 2, 1]))