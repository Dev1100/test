class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def sum(tree):
    if (tree == None):
        return 0
    return (tree.value + sum(tree.left) +
                       sum(tree.right))


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    d = sum(tree)

    print("Сумма", d)

