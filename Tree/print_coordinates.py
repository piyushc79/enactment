"""
Print Coordinate of all Tree nodes: Given a Binary Tree. Assuming each node denotes some
x,y coordinate. root node denotes (0,0). Write a code to display coordinate of all nodes
                   --------
                   | Tree |
                   --------
                      4
                    /   \
                   2    6
                /   \ /   \
               1    3 5   7
Output:
Coordinate of 4 : (0,0), Coordinate of 2 : (-1,-1), Coordinate of 3 :
(1,-1), Coordinate of 1 : (-2,-2), Coordinate of 3 : (0,-2) etc.
"""


class Tree(object):
    """
    Class for creating Tree
    """
    def __init__(self, data):
        """
        Initialization
        """
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def create_bst(a, left, right):
        """
        Create BST
        """
        if right < left:
            return None

        mid = (left+right)/2

        root = Tree(a[mid])

        root.left = Tree.create_bst(a, left, mid-1)
        root.right = Tree.create_bst(a, mid+1, right)

        return root


def print_coordinate(root, x, y):
    """
    Print Tree co-ordinates
    """
    if not root:
        return None

    print root.data, x, y

    print_coordinate(root.left, x-1, y-1)
    print_coordinate(root.right, x+1, y-1)


if __name__ == "__main__":
    print "Print Tree's node co-ordinates"
    data = [1,2,3,4,5,6,7]
    tree = Tree.create_bst(data, 0, len(data)-1)
    print_coordinate(tree, 0,0)