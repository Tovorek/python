class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
def getMinimumKey(curr):
    while curr.left:
        curr = curr.left
    return curr
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def deleteNode(root, key):
    parent = None
    curr = root
    while curr and curr.data != key:
        parent = curr
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    if curr is None:
        return root
    if curr.left is None and curr.right is None:
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None
    elif curr.left and curr.right:
        successor = getMinimumKey(curr.right)
        val = successor.data
        deleteNode(root, successor.data)
        curr.data = val
    else:
        if curr.left:
            child = curr.left
        else:
            child = curr.right
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            root = child
 
    return root
 
 
if __name__ == '__main__':
 
    keys = [15, 10, 20, 8, 12, 16]
 
    root = None
    for key in keys:
        root = insert(root, key)
 
    root = deleteNode(root, 16)
    inorder(root)