class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            node = self.root

            while node:
                if data < node.data:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(data)
                        return
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(data)
                        return

    def __insert_recursively(self, node, data):
        if data < node.data:
            if node.left:
                self.__insert_recursively(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.__insert_recursively(node.right, data)
            else:
                node.right = Node(data)

    def insert_recursively(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.__insert_recursively(self.root, data)

    def print_transversal_inorder(self):
        stack = []
        current_node = self.root

        while current_node or stack:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                tmp = stack.pop()
                print(tmp.data, end=' ')
                current_node = tmp.right
        print('\n')

    def print_transversal_inorder_recursively(self, node):
        if node.left:
            self.print_transversal_inorder_recursively(node.left)

        print(node.data)

        if node.right:
            self.print_transversal_inorder_recursively(node.right)

    def get_first_inorder(self, node):
        while node:
            if node.left:
                node = node.left
            else:
                return node

    def delete_recursively(self, node, data):
        if data < node.data:
            node.left = self.delete_recursively(node.left, data)
        elif data > node.data:
            node.right = self.delete_recursively(node.right, data)
        else:
            if node.right and node.left:
                first_inorder = self.get_first_inorder(node.right)
                node.data = first_inorder.data
                node.right = self.delete_recursively(node.right, node.data)
            elif node.left:
                return node.left
            else:
                return node.right
        return node


bst = BST()
bst.insert_recursively(10)
bst.insert_recursively(5)
bst.insert_recursively(15)
bst.insert_recursively(2)
bst.insert_recursively(6)

bst.print_transversal_inorder()

# bst.delete_recursively(bst.root, 2)
# bst.delete_recursively(bst.root, 6)
bst.delete_recursively(bst.root, 10)

bst.print_transversal_inorder()

print('Done!')
