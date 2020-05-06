def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def permute(index, array):
    for i in range(index, len(array)):
        if index < len(array) - 1:
            swap(array, index, i)
            permute(index + 1, array)
            swap(array, index, i)
        else:
            print(array)


term = 'abc'

permute(0, list(term))
