class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder_traversal(node):
    """
    Perform in-order traversal of the binary tree.
    """
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)


def preorder_traversal(node):
    """
    Perform pre-order traversal of the binary tree.
    """
    if node:
        print(node.val, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def postorder_traversal(node):
    """
    Perform post-order traversal of the binary tree.
    """
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val, end=" ")


# Test the binary tree
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal: ")
    inorder_traversal(root)
    print("\nPreorder traversal: ")
    preorder_traversal(root)
    print("\nPostorder traversal: ")
    postorder_traversal(root)
