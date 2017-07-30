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


def find_max_using_level_order(root):
    if not root:
        return None
    max_data = None
    queue_stack = [root]
    while queue_stack:
        node = queue_stack.pop(0)
        if node.data > max_data:
            max_data = node.data
        if node.left:
            queue_stack.append(node.left)
        if node.right:
            queue_stack.append(node.right)
    return max_data


def find_recursive(root, data):
    if not root:
        return False
    if root.data == data:
        return True
    is_find = find_recursive(root.left, data)
    if not is_find:
        is_find = find_recursive(root.right, data)
    return is_find


def find_using_level_order(root, data):
    if not root:
        return None
    queue_stack = [root]

    while queue_stack:
        node = queue_stack.pop(0)
        if node.data == data:
            return True
        if node.left:
            queue_stack.append(node.left)
        if node.right:
            queue_stack.append(node.right)
    return False


def insert_in_binary_tree_using_level_order(root, data):
    if data is None:
        return None

    new_node = BinaryTreeNode(data)
    if not root:
        root = new_node
        return root

    queue_stack = [root]
    while queue_stack:
        node = queue_stack.pop(0)
        if node.data == data:
            return root
        if node.left:
            queue_stack.append(node.left)
        else:
            node.left = new_node
            return root
        if node.right:
            queue_stack.append(node.right)
        else:
            node.right = new_node
            return root


def find_size_recursive(root):
    if not root:
        return 0
    return find_size_recursive(root.left) + find_size_recursive(root.right) + 1


def find_size_by_using_level_traversal(root):
    if not root:
        return 0
    queue_stack = [root]
    count = 0
    while queue_stack:
        node = queue_stack.pop(0)
        count += 1
        if node.left:
            queue_stack.append(node.left)
        if node.right:
            queue_stack.append(node.right)
    return count


def level_order_traversal_in_reverse(root):
    if not root:
        return None

    queue = [root]
    stack = []
    while queue:
        node = queue.pop(0)
        stack.append(node.data)

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    stack.reverse()
    for data in stack:
        print data,


def max_path_sum_util(root, res):
    # Base Case
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.data

    # Find maximum sum in left and right subtree. Also
    # find maximum root to leaf sums in left and right
    # subtrees ans store them in ls and rs
    ls = max_path_sum_util(root.left, res)
    rs = max_path_sum_util(root.right, res)

    # If both left and right children exist
    if root.left is not None and root.right is not None:
        # update result if needed
        res[0] = max(res[0], ls + rs + root.data)

        # Return maximum possible value
        # for root being on one side
        return max(ls, rs) + root.data

    # If any of the two children is empty, return
    # root sum for root being on one side
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data


# The main function which returns sum of the maximum
# sum path between two leaves. This function mainly
# uses max_path_sum_util()
def max_path_sum(root):
    if not root:
        return 0

    res = [root.data]
    max_path_sum_util(root, res)
    return res[0]


# def print_vector(v):
#     print ', '.join(map(str, v))
#
#
# def print_path_sum_util(root, path):
#     if not root:
#         return 0
#
#     path.append(root.data)
#
#     print_path_sum_util(root.left, path)
#     print_path_sum_util(root.right, path)
#
#     if not(root.left and root.right):
#         print_vector(path)
#     else:
#         path.append(None)
#     pop_data = path.pop()
#     while pop_data is not None and path:
#         pop_data = path.pop()
#
#
# def print_path_sum(root):
#     path = []
#     print_path_sum_util(root, path)


def path_finder(root, val, path, paths):
    # import ipdb; ipdb.set_trace()
    if not root:
        return False

    if not root.left and root.right:
        if root.data == val:
            path.append(root.data)
            paths.append(path)
            return True
        else:
            return False

    left = path_finder(root.left, val-root.data, path, paths)
    right = path_finder(root.right, val-root.data, path, paths)
    return left or right


def has_path_with_sum(root, val):
    paths = []
    path_finder(root, val, [], paths)
    print 'Sum: {}'.format(val)
    print 'paths: {}'.format(paths)


i = 0


def build_tree_from_pre_order(A):
    global i
    if not A or i>len(A):
        return None, i

    new_node = BinaryTreeNode(A[i])
    if A[i] == 'L':
        return new_node

    i += 1
    new_node.left = build_tree_from_pre_order(A)

    i += 1
    new_node.right = build_tree_from_pre_order(A)

    return new_node


def print_statement(root):
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
    print "----Level Order Traversal In Reverse----"
    level_order_traversal_in_reverse(root)
    print '\n'

if __name__ == "__main__":
    # data = [1,2,3,4,5,6,7]
    # root = BinaryTreeNode.create_tree(data)
    # print_statement(root)
    #
    # print 'Maximum path sum value: {}'.format(max_path_sum(root))
    # print 'find_max_recursive: ', find_max_recursive(root)
    #
    # print 'find_max_using_level_order: ', find_max_using_level_order(root)
    #
    # print 'find_recursive 7: ', find_recursive(root, 7)
    # print 'find_recursive 9: ', find_recursive(root, 9)
    #
    # print 'find_using_level_order 7: ', find_using_level_order(root, 7)
    # print 'find_using_level_order 9: ', find_using_level_order(root, 9)
    # print 'Size of tree before inserting new element: ', find_size_by_using_level_traversal(root)
    # root = insert_in_binary_tree_using_level_order(root, 8)
    # print 'Size of tree after inserting new element: ', find_size_by_using_level_traversal(root)
    # print 'Tree Traversal after inserting element'
    # print_statement(root)
    # print 'Maximum path sum value: {}'.format(max_path_sum(root))
    # root = BinaryTreeNode(1)
    # root.left = BinaryTreeNode(3)
    # root.left.left = BinaryTreeNode(2)
    # root.left.right = BinaryTreeNode(1)
    # root.right = BinaryTreeNode(-1)
    # root.right.left = BinaryTreeNode(4)
    # root.right.left.left = BinaryTreeNode(1)
    # root.right.left.right = BinaryTreeNode(2)
    # root.right.right = BinaryTreeNode(5)
    # root.right.right.right = BinaryTreeNode(2)
    # has_path_with_sum(root, 5)
    # s = 21
    # root = BinaryTreeNode(10)
    # root.left = BinaryTreeNode(8)
    # root.right = BinaryTreeNode(2)
    # root.left.right = BinaryTreeNode(5)
    # root.left.left = BinaryTreeNode(3)
    # root.right.left = BinaryTreeNode(2)
    # print has_path_with_sum(root, s)
    A = ['I', 'I', 'L', 'I', 'L', 'L', 'I', 'L', 'L']
    root = build_tree_from_pre_order(A)
    print 'input: {}'.format(' '.join(A))
    preorder_recursive(root)
    print '\n'
    postorder_recursive(root)