class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySerchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        
        if self.root == None:
            self.root = new_node
            return True

        temp = self.root
        
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def contains(self, value):
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


tree = BinarySerchTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)

print(tree.contains(2))
print(tree.contains(12))
# print(tree.root.value)
# print(tree.root.left.value)
# print(tree.root.right.value)
