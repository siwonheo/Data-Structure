class Node:
    def __init__(self, item, left_child = None, right_child = None):
        self.key = item
        self.left = left_child
        self.right = right_child

    def get_key(self):
        return self.key

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_key(self, new_key):
        self.key = new_key

    def set_left(self, new_left_child):
        self.left = new_left_child

    def self_right(self, new_right_child):
        self.right = new_right_child

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        if node != None:
            print(str(node.get_key()), ' ', end = ' ')
            if node.get_left():
                self.preorder(node.get_left())
            if node.get_right():
                self.preorder(node.get_right())

    def inorder(self, node):
        if node != None:
            if node.get_left():
                self.inorder(node.get_left())
            print(str(node.get_key()), ' ', end=' ')
            if node.get_right():
                self.inorder(node.get_right())

    def postorder(self, node):
        if node != None:
            if node.get_left():
                self.postorder(node.get_left())
            if node.get_right():
                self.postorder(node.get_right())
            print(str(node.get_key()), ' ', end=' ')

    def levelorder(self, root):
        q = Queue()
        q.enqueue(root)
        while not q.is_empty():
            node = q.dequeue()
            print(str(node.get_key()), ' ', end = ' ')
            if node.get_left():
                q.enqueue(node.get_left())
            if node.get_right():
                q.enqueue(node.get_right())





if __name__ == "__main__":
    a = Node(10)
    print(a.get_key())
    print(a.get_left())
    print(a.get_right())
    b = Node(15)
    a.set_left(b)
    print(a.get_left().get_key())
