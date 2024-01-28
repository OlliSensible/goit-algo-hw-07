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

def find_sum(node):
    if node is None:
        return 0
    return node.val + find_sum(node.left) + find_sum(node.right)

if __name__ == "__main__":
    root = Node(5)
    for key in [3, 7, 2, 8, 6, 4]:
        root = insert(root, key)

    print("Сума всіх значень в дереві:", find_sum(root))