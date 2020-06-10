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
                    return node.value

        def __delete(node, _value):
            if _value == node.value:
                if node.left and node.right:
                    new_value = __get_left_most(node.right)
                    __delete(node, new_value)
                    node.value = new_value
                elif node.left:
                    return node.left
                elif node.right:
                    return node.right
                else:
                    return None

            elif _value < node.value:
                node.left = __delete(node.left, _value)
            else:
                node.right = __delete(node.right, _value)

            return node

        __delete(self.root, value)


bst = BST()
bst.r_add(5)
bst.r_add(2)
bst.add(7)
bst.add(1)
bst.r_add(3)
bst.add(6)
bst.r_add(8)
bst.r_add(9)

# bst.r_print_transversal()
# bst.delete(i)
bst.transversal_inorder()
bst.transversal_preorder()
bst.transversal_postorder()
