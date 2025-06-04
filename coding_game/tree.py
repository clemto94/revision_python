"""
A tree is composed of nodes which follow these rules:
A node holds a value corresponding to an integer. Except the root node of the tree, a node is always
referenced by only one other node. A node has no more than two children. They are called left child and
right child. If a node has no right or left child, the corresponding reference is None. All the descendants
to the left of a node are smaller than the node, and all the descendants to the right of the node are
greater than the node.

Here is an example of such a tree (the root node holds integer 9):

Fig. 1

To simplify things, we combine everything into a single class named Node. The height of the tree is
between 0 and 100 000 nodes (the height of a tree is the length of the path from the root to the deepest
node in the tree). Question: Implement the function find(node, value) which returns the node
holding the given value. If the node doesn't exist, then find should return None. Important note: Try
to save memory (RAM) space. To test your solution, you have access to two example trees: The variable
small contains the root node of the tree from Fig. 1. The variable large contains the root node of a
tree of height 100 000 nodes. The deepest node holds 0.
"""


class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v


def find(node, value):
    curr = node
    while curr:
        if curr.value == value:
            return curr
        elif value < curr.value:
            curr = curr.left
        else:
            curr = curr.right
    return None

