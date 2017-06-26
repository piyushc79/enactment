"""
Binary Tree Class and its methods
"""


class BinaryTreeNode:
    def __init__(self, data):
        """
        initialization
        """
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        """
        set data
        """
        self.data = data

    def get_data(self):
        """
        get data
        """
        return self.data

    def get_left(self):
        """
        get left child of a node
        """
        return self.left

    def get_right(self):
        """
        get right child of a node
        """
        return self.right

    @staticmethod
    def create_tree(data):
        """
        Create BST
        """
        if not data:
            return None

        mid = len(data)/2
        root = BinaryTreeNode(data[mid])

        root.left = BinaryTreeNode.create_tree(data[:mid])
        root.right = BinaryTreeNode.create_tree(data[mid+1:])
        return root


def preorder_recursive(root):
    if not root:
        return None

    print root.data,

    preorder_recursive(root.left)
    preorder_recursive(root.right)


def preorder_iterative(root):
    if not root:
        return None

    stack = [root]

    while stack:

        node = stack.pop()
        print node.data,

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)



def postorder_recursive(root):
    if not root:
        return None

    postorder_recursive(root.left)
    postorder_recursive(root.right)

    print root.data,


def postorder_iterative(root):
    if not root:
        return None

    visited = set()
    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                print node.data,
                node = None


def inorder_recursive(root):
    if not root:
        return None

    inorder_recursive(root.left)
    print root.data,
    inorder_recursive(root.right)


def inorder_iterative(root):
    if not root:
        return None

    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print node.data,
            node = node.right


def level_order(root):
    if not root:
        return None

    queue_stack = [root]
    node = None

    while queue_stack:
        node = queue_stack.pop(0)
        print node.data,

        if node.left:
            queue_stack.append(node.left)
        if node.right:
            queue_stack.append(node.right)

max_data = None


def find_max_recursive(root):
    global max_data

    if not root:
        return None

    if root.data > max_data:
            max_data = root.data

    find_max_recursive(root.left)
    find_max_recursive(root.right)
    return max_data

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7]
    root = BinaryTreeNode.create_tree(data)
    print "-----Preorder  Iterative-----"
    preorder_iterative(root)
    print '\n'
    print "-----Preorder  Recursive-----"
    preorder_recursive(root)
    print '\n'
    print "----Postorder   Iterative----"
    postorder_iterative(root)
    print '\n'
    print "----Postorder   Recursive----"
    postorder_recursive(root)
    print '\n'
    print "-----Inorder   Iterative-----"
    inorder_iterative(root)
    print '\n'
    print "-----Inorder   Recursive-----"
    inorder_recursive(root)
    print '\n'
    print "----Level Order Traversal----"
    level_order(root)
    print '\n'

    max_data = find_max_recursive(root)
    print max_data