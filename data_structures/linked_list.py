class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.node = None

    def add(self, val):
        if self.node is None:
            self.node = Node(val)
            return
        
        node = self.node
        while node:
            if node.next:
                node = node.next
            else:
                node.next = Node(val)
                return

    def print_list(self):
        if self.node:
            node = self.node
            while node:
                print(node.val, end=' ')
                node = node.next
        print('\n')

l_list = LinkedList()
l_list.add(1)
l_list.add(2)
l_list.add(3)
            
l_list.print_list()
