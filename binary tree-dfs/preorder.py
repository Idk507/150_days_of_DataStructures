def preorder(root):
    if not root:
        return []
    return [root.data] + preorder(root.left) + preorder(root.right)
