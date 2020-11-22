class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
        else:
            tmp = self.root

            while tmp:
                if value < tmp.value:
                    if tmp.left:
                        tmp = tmp.left
                    else:
                        tmp.left = node
                        break
                else:
                    if tmp.right:
                        tmp =  tmp.right
                    else:
                        tmp.right = node
                        break

    def r_add(self, value):
        def __add(node, _value):
            if not node:
                return Node(value)
            elif _value < node.value:
                node.left = __add(node.left, _value)
            else:
                node.right = __add(node.right, _value)
            return node

        self.root = __add(self.root, value)

    # left -> root -> right
    # stack is used just to store the parent node and get its children afterwards
    # tmp_node is used to store the node that will be processed
    def transversal_inorder(self):
        stack = []
        tmp = self.root

        while tmp or stack:
            if tmp:
                stack.append(tmp)
                tmp = tmp.left
            else:
                tmp = stack.pop()
                print(tmp.value, end=' ')
                tmp = tmp.right
        print('\n')

    # root -> left -> right
    def transversal_preorder(self):
        stack = [self.root]

        while stack:
            tmp_node = stack.pop()
            print(tmp_node.value, end=' ')

            if tmp_node.right:
                stack.append(tmp_node.right)
            if tmp_node.left:
                stack.append(tmp_node.left)

        print('\n')

    # left -> right -> root
    def transversal_postorder(self):
        stack = [self.root]
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
            print(tmp_node.value, end=' ')

        print('\n')

    def r_print_transversal(self):

        def __print(node):
            if node:
                __print(node.left)
                print(node.value, end=' ')
                __print(node.right)
        print('\n')

        __print(self.root)


    def delete(self, value):
        def __get_left_most(node):
            while node:
                if node.left:
                    node = node.left
                else:
                    break
            return node

        def __delete(node, value):
            if node.value == value:
                if node.left and node.right:
                    tmp = __get_left_most(node.right)
                    node.value = tmp.value
                    node.right = __delete(node.right, tmp.value)
                    return node
                elif node.left:
                    return node.left
                elif node.right:
                    return node.right
            else:
                if value < node.value:
                    node.left = __delete(node.left, value)
                else:
                    node.right = __delete(node.right, value)
                return node

        self.root = __delete(self.root, value)


bst = BST()
bst.add(5)
bst.add(2)
bst.add(7)
bst.add(1)
bst.add(3)
# bst.add(6)
# bst.r_add(8)
# bst.r_add(9)

# bst.r_print_transversal()
bst.transversal_inorder()
bst.delete(2)
bst.transversal_inorder()
# bst.transversal_preorder()
# bst.transversal_postorder()
