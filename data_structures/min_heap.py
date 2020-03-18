def swap(heap, i, j):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp

def bubble_up(heap):
    idx = len(heap) - 1
    while idx > 0:
        parent_idx = int(idx/2)
        if heap[idx] < heap[parent_idx]:
            swap(heap, idx, parent_idx)
            idx = parent_idx
        else:
            break

def bubble_down(heap):
    idx = 0
    while idx * 2 + 1 < len(heap):
        left = (idx + 1) * 2 - 1
        right = (idx + 1) * 2

        min_idx = None
        if heap[left] < heap[right]:
            min_idx = left
        else:
            min_idx = right

        if heap[idx] > heap[min_idx]:
            swap(heap, idx, min_idx)
            idx = min_idx
        else:
            break

def insert(heap, data):
    heap.append(data)
    bubble_up(heap)

def extract_min(heap):
    heap[0] = heap[-1]
    heap.pop()
    bubble_down(heap)

heap = []
insert(heap, 2)
insert(heap, 3)
insert(heap, 4)
insert(heap, 5)
insert(heap, 6)
insert(heap, 7)
insert(heap, 8)
insert(heap, 1)

print(heap)

extract_min(heap)

print(heap)