class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        elif not self.tail:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_start(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_before(self, val, new_val):
        if not self.head or (self.head and self.head.val == val):
            self.add_start(new_val)
        else:
            cur = self.head
            while cur.next:
                if cur.next.val == val:
                    new_node = Node(new_val)
                    new_node.next = cur.next
                    cur.next = new_node
                    return
                else:
                    cur = cur.next

    def add_after(self, val, new_val):
        if not self.head:
            self.add_start(new_val)
        elif self.tail and self.tail == val:
            self.add_end(new_val)
        else:
            cur = self.head

            while cur and cur.val != val:
                cur = cur.next

            if cur:
                new_node = Node(new_val)
                new_node.next = cur.next
                cur.next = new_node

    def delete(self, val):
        if self.head and self.head.val == val:
            self.head = self.head.next
            return

        cur = self.head

        while cur.next:
            if cur.next.val == val:
                if self.tail == cur.next:
                    self.tail = cur
                cur.next = cur.next.next
                return
            else:
                cur = cur.next
        

    def find(self, val):
        cur = self.head
        i = 0
        while cur:
            if cur.val == val:
                return i
            cur = cur.next
            i += 1

    def print_list(self):
        print('head - {} / tail - {}'.format(self.head.val, self.tail.val))
        if self.head:
            node = self.head
            while node:
                print(node.val, end=' ')
                node = node.next
        print('\n')

l_list = LinkedList()
l_list.add_end(1)
l_list.add_end(2)
l_list.add_end(3)
l_list.add_end(4)
l_list.add_start(0)
l_list.add_end(7)
l_list.add_before(7, 5)
l_list.add_after(5, 6)
            
l_list.print_list()

l_list.delete(1)
            
l_list.print_list()

l_list.delete(0)
l_list.delete(7)
l_list.print_list()

print(l_list.find(7))