class MinHeap:

    def __init__(self):
        self._list = []

    def swap(self, i, j):
        tmp = self._list[i]
        self._list[i] = self._list[j]
        self._list[j] = tmp

    def bubble_up(self):
        idx_child = len(self._list) - 1

        while idx_child > 0:
            idx_parent = int((idx_child - 1) / 2)
            if self._list[idx_child] < self._list[idx_parent]:
                self.swap(idx_child, idx_parent)
                idx_child = idx_parent
            else:
                break

    def add(self, value):
        self._list.append(value)
        self.bubble_up()

    def bubble_down(self, idx_parent):
        # left child
        idx_child = idx_parent * 2 + 1

        while idx_child < len(self._list) - 1:
            # right child
            idx_right_child = idx_parent * 2 + 2

            # check if there is right child
            # and get min(left_child, right_child)
            if (idx_right_child < len(self._list) - 1
                and self._list[idx_right_child] < self._list[idx_child]):
                idx_child = idx_right_child

            # compare parent with smallest child
            if self._list[idx_parent] > self._list[idx_child]:
                self.swap(idx_parent, idx_child)
                idx_parent = idx_child
                idx_child = idx_parent * 2 + 1
            else:
                break

    def remove(self, value):
        parent = 0
        for i in range(len(self._list)):
            if self._list[i] == value:
                parent = i
                break

        self._list[parent] = self._list.pop()
        self.bubble_down(parent)


min_heap = MinHeap()
# min_heap.add(5)
# min_heap.add(2)
# min_heap.add(3)
# min_heap.add(6)
# min_heap.add(7)
# min_heap.add(8)
# min_heap.add(1)

# print(min_heap._list)

min_heap._list = [1,5,2,6,7,3,8,20,21,22,23,24,25,26]
min_heap.remove(1)

print(min_heap._list)