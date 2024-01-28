import uuid

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

if __name__ == "__main__":
    root = Node(5)
    for key in [3, 7, 2, 8, 6, 4]:
        root = insert(root, key)

    print("Найменше значення в дереві:", find_min_value(root))