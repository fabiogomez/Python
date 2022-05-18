
# Python program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree

class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

def print_inorder(root):
    if root:
        #First  recur on left child 
        print_inorder(root.left)

        print(root.val)

        # Now recur ib rigth child 
        print_inorder(root.right)


def print_postorder(root):

    if root:

        #First recur on left child
        print_postorder(root.left)

        #the recur on rigth child
        print_postorder(root.right)

        #now print data of node
        print(root.val)


def print_preorder(root):

    if root:
        #now print data of node
        print(root.val)

        #First recur on left child
        print_preorder(root.left)

        #the recur on rigth child
        print_preorder(root.right)


root= Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal of binary tree is")
print_preorder(root)

print("\nInorder traversal of binary tree is")
print_inorder(root)

print ("\nPostorder traversal of binary tree is")
print_postorder(root)





        