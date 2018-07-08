root = [10,5,-3,3,2,None,11,3,-2,None,1]
# root=[1,2,3,4,5]
sum = 8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def addChild(node, root, pos):
    if (pos*2+1)<len(root):
        node.left = TreeNode(root[pos*2+1])
        addChild(node.left, root, pos*2+1)
    if (pos*2+2)<len(root):
        node.right = TreeNode(root[pos*2+2])
        addChild(node.right, root, pos*2+2)

def createTree(root):
    if len(root)==0:
        print(None)
    tree = TreeNode(root[0])
    addChild(tree, root, 0)
    return tree

def inorder(node):
    if node is None:
        return
    if node.left:
        inorder(node.left)
    print(node.val)
    if node.right:
        inorder(node.right)

# inorder(tree)

def preorder(node):
    if node is None:
        return
    print(node.val)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)
# preorder(tree)

def postorder(node):
    if node is None:
        return
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.val)
# postorder(tree)