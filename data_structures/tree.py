class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, data):
        self.root = Node(data)


    def insert(self, data):
        '''
        Insert the key into the binary tree at first position available in level order.
        '''
        _list = [self.root]
        while(_list):
            node = _list.pop(0)

            if node.left:
                _list.append(node.left)
            else:
                node.left = Node(data)
                break

            if node.right:
                _list.append(node.right)
            else:
                node.right = Node(data)
                break

    def get_height(self, node):
        left, right = 1, 1
        if node.left:
            left = self.get_height(node.left) + 1
        if node.right:
            right = self.get_height(node.right) + 1

        return max(left, right)

    def transversal_inorder_recursively(self, node):
        if node.left:
            self.transversal_inorder_recursively(node.left)
        
        print(node.data, end=' ')

        if node.right:
            self.transversal_inorder_recursively(node.right)

    def transversal_inorder_satck(self, node):
        stack = []
        tmp_node = node

        while True:
            
            if tmp_node:
                stack.append(tmp_node)
                tmp_node = tmp_node.left
            elif (stack):
                tmp_node = stack.pop()
                print(tmp_node.data, end=' ')
                tmp_node = tmp_node.right
            else:
                break
                
    def delete(self, data):
        _list = [self.root]
        node_to_delete = None
        deepest_rightmost = None
        while _list:
            deepest_rightmost = _list.pop(0)

            if deepest_rightmost.data == data:
                node_to_delete = deepest_rightmost

            if deepest_rightmost.left:
                _list.append(deepest_rightmost.left)

            if deepest_rightmost.right:
                _list.append(deepest_rightmost.right)

        if node_to_delete:
            print(node_to_delete.data, deepest_rightmost.data)

    
tree = Tree(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.transversal_inorder_recursively(tree.root)
print('\n')
tree.transversal_inorder_satck(tree.root)
print('\n')
print(tree.get_height(tree.root))

# tree.delete(2)