'''
inorder = lef roo ri
preorder  root lef right
postorder left right root


'''

import random

class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def inorder(root):
    if(root==None):
        return
    else:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
def preorder(root):
    if(root==None):
        return
    else:
        print(root.value)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if(root==None):
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

def buildTree(n):
    if n == 0:
        return None
    node = Node(random.randint(1, 100))
    node.left = buildTree(n - 1)
    node.right = buildTree(n - 1)
    return node

root = buildTree(4)
inorder(root)
