class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST2DLL:
    def __init__(self, debug=False):
        self.debug = debug

    def print_debug(self, msg):
        if self.debug:
            print msg

    def convert_helper(self, current_node, tail_node_container):
        # Base case
        if current_node is None:
            return None

        self.print_debug("Entering node {}".format(current_node.data))

        # right sub-tree
        tail_node_right_container = [None]

        dll_right = self.convert_helper(
            current_node.right, tail_node_right_container)

        if dll_right is not None:
            # Change boundary links
            dll_right.left = current_node
            current_node.right = dll_right

            self.print_debug(
                "Current node {}, setting tail node {}".format(
                    current_node.data, tail_node_right_container[0].data))

            tail_node_container[0] = tail_node_right_container[0]
        else:
            # no right sub-tree exists
            self.print_debug(
                "Current node {}, right node is None, setting tail node {}".format(
                    current_node.data, current_node.data))

            tail_node_container[0] = current_node

        # left sub-tree
        tail_node_left_container = [None]

        dll_left = self.convert_helper(
            current_node.left, tail_node_left_container)

        if dll_left is not None:
            # Change boundary links
            current_node.left = tail_node_left_container[0]
            tail_node_left_container[0].right = current_node

            self.print_debug("Current node {}, return head node {}".format(
                current_node.data, dll_left.data))
            return dll_left
        else:
            # no left sub-tree exists
            self.print_debug(
                "Current node {}, left node is None, return head node {}".format(
                    current_node.data, current_node.data))

            return current_node

    def convert(self, root_node):
        container = [None]
        return self.convert_helper(root_node, container)
