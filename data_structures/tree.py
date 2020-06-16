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
            node = _list.pop()

            if not node.left:
                node.left = Node(data)
                break
            elif not node.right:
                node.right = Node(data)
                break
            
            if node.right:
                _list.append(node.right)
            if node.left:
                _list.append(node.left)

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

    # left -> root -> right
    # stack is used just to store the parent node and get its children afterwards
    # tmp_node is used to store the node that will be processed
    def transversal_inorder_satck(self, node):
        stack = []
        tmp_node = node

        while tmp_node or stack:
            if tmp_node:
                stack.append(tmp_node)
                tmp_node = tmp_node.left
            elif stack:
                tmp_node = stack.pop()
                print(tmp_node.data, end=' ')
                tmp_node = tmp_node.right

    # root -> left -> right
    def transversal_preorder(self, node):
        stack = [node]

        while stack:
            tmp_node = stack.pop()
            print(tmp_node.data, end=' ')

            if tmp_node.right:
                stack.append(tmp_node.right)
            if tmp_node.left:
                stack.append(tmp_node.left)

    # left -> right -> root
    def transversal_postorder(self, node):
        stack = [node]
        stack_out = []

        while stack:
            tmp_node = stack.pop()
            stack_out.append(tmp_node)
            
            if tmp_node.left:
                stack.append(tmp_node.left)
            if tmp_node.right:
                stack.append(tmp_node.right)

        while stack_out:
            tmp_node = stack_out.pop()
            print(tmp_node.data, end=' ')

    def delete(self, _data):
        def __get_right_most(node):
            if node.right:
                return self.get_right_most(node.right)
            else:
                return node

        def __delete(node, data):
            if node.data == data:
                if not node.left:
                    tmp = node.right
                    node = None
                    return tmp
                elif not node.right:
                    tmp = node.left
                    node = None
                    return tmp
                
                tmp = __get_right_most(node.left)
                node.data = tmp.data
                node.left = __delete(node.left, tmp.data)
            else:
                if node.left:
                    node.left = __delete(node.left, data)

                if node.right:
                    node.right = __delete(node.right, data)

            return node

        self.root = __delete(self.root, _data)

    def breadth_first_search(self, node):

        queue = [node]

        while queue:
            current_node = queue.pop(0)

            print(current_node.data, end=' ')

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

    
tree = Tree(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
# tree.insert(6)
# tree.insert(7)
# tree.transversal_inorder_recursively(tree.root)
# print('\n')
# # tree.transversal_inorder_satck(tree.root)
# print('\n')
# print(tree.get_height(tree.root))
tree.breadth_first_search(tree.root)
print('\n')
tree.delete(2)
tree.breadth_first_search(tree.root)
print('\n')


# tree.transversal_preorder(tree.root)
# tree.transversal_postorder(tree.root)
