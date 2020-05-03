class MinHeap:

    def __init__(self):
        self._list = []

    def swap(self, i, j):
        tmp = self._list[i]
        self._list[i] = self._list[j]
        self._list[j] = tmp

    def bubble_up(self):
        child = len(self._list) - 1

        while child > 0:
            parent = int((child - 1) / 2)
            if self._list[child] < self._list[parent]:
                self.swap(child, parent)
                child = parent
            else:
                break

    def add(self, value):
        self._list.append(value)
        self.bubble_up()

    def bubble_down(self, parent):
        child = parent * 2 + 1

        while child < len(self._list) - 1:
            right_child = parent * 2 + 2

            if right_child < len(self._list) - 1 and self._list[child] > self._list[right_child]:
                child = self._list[right_child]

            if self._list[parent] > self._list[child]:
                self.swap(parent, child)
                parent = child
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
min_heap.add(5)
min_heap.add(2)
min_heap.add(3)
min_heap.add(6)
min_heap.add(7)
min_heap.add(8)
min_heap.add(1)

print(min_heap._list)

min_heap.remove(1)

print(min_heap._list)
