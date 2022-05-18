class Node:

    def __init__(self, data):
        #left child
        self.left = None
        #right child
        self.right = None
        #node's value
        self.data = data
    #getters
    def setLeft(self, node):
        self.left = node
    def setRight(self, node):
        self.right = node

    #setters
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

    def printTree(self):
        if self.getLeft():
            self.getLeft().printTree()
        print(self.data)
        if self.getRight():
            self.getRight().printTree()


    def insert(self, data):
        if  data < self.data:
            if self.getLeft() is None:
                self.setLeft(Node(data))
            else:
                self.getLeft().insert(data)
        elif data > self.data: 
            if self.getRight() is None:
                self.setRight(Node(data))
            else:
                self.getRight().insert(data)

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" is not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" is not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " is found"


root = Node(30)
root.insert(14)
root.insert(34)
root.insert(15)
root.insert(61)
root.insert(84)
root.insert(22)
root.insert(100)
#root.printTree()


print(root.getLeft().data)
print(root.getRight().getRight().getRight().getRight().data)

    
