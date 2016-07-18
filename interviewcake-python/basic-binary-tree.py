class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self, data):
        #if data already exists - DO NOT insert
        #if data at root greater than data, insert at left
        #if data at root smaller than data, insert at right
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    def preOrder(self):
        if self:
            print self.value
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
    def inOrder(self):
        if self:
            if self.left:
                self.left.preOrder()
            print self.value
            if self.right:
                self.right.preOrder()
    def postOrder(self):
        if self:
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
            print self.value

class Tree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preOrder(self):
        if self.root:
            print "PRE-ORDER"
            self.root.preOrder()
    def inOrder(self):
        if self.root:
            print "IN-ORDER"
            self.root.inOrder()
    def postOrder(self):
        if self.root:
            print "POST-ORDER"
            self.root.postOrder()

obj = Tree()
print obj.insert(20)
print obj.insert(13)
print obj.insert(17)
print obj.insert(11)
print obj.insert(15)
print obj.insert(24)
obj.preOrder()
obj.postOrder()
obj.inOrder()
