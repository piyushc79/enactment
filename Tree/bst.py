class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


def find_recursive(root, data):
    current_node = root
    while current_node is not None and data != current_node.get_data():
        if data > current_node.get_data():
            current_node = current_node.get_right()
        else:
            current_node = current_node.get_left()
    return current_node


def find_iterative(root, data):
    current_node = root
    while current_node:
        if data == current_node.get_data():
            return current_node
        if data < current_node.get_data():
            current_node = current_node.get_left()
        else:
            current_node = current_node.get_right()
    return None


def find_min_recursive(root):
    current_node = root
    if current_node.get_left() is None:
        return current_node
    else:
        return find_min_recursive(current_node.get_left())


def find_min_iterative(root):
    current_node = root
    if current_node is None:
        return current_node
    while current_node.get_left() is not None:
        current_node = current_node.get_left()
    return current_node


def find_max_recursive(root):
    current_node = root
    if current_node.get_right() is None:
        return current_node
    else:
        find_max_recursive(current_node.get_right())


def find_max_iterative(root):
    current_node = root
    if current_node is None:
        return current_node
    while current_node.get_right() is not None:
        current_node = current_node.get_right()
    return current_node


def successor_bst(root):
    temp = None
    if root.get_right():
        temp = root.get_right()
        while temp.get_left():
            temp = temp.get_left()
    return temp


def predecessor_bst(root):
    temp = None
    if root.get_left():
        temp = root.get_left()
        while temp.get_right():
            temp = temp.get_right()
    return temp


def insert_node(root, node):
    if root is None:
        root = node
    else:
        if root.get_data() > node.get_data():
            if root.get_left() is None:
                root.left = node
            else:
                insert_node(root.get_left(), node)
        else:

            if root.get_right() is None:
                root.right = node
            else:
                insert_node(root.right, node)



if __name__ ==  '__main__':
    root = BSTNode(4)
    items = [7, 2, 6, 9, 3, 1, 8, 5]
    for i in items:
        ith_node = BSTNode(i)
        insert_node(root, ith_node)
    from binarytree import print_statement
    print_statement(root)
