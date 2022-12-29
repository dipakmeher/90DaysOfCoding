#Find the height of a given tree
from binarytree import Node
#Function
def HeightOfTree(root):
    #BC
    if(root is None):
        return 0
    
    #Hypothesis
    left = HeightOfTree(root.left)
    right = HeightOfTree(root.right)

    #Tndudction
    return 1+max(left,right)

#Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(root)
print("Height of a tree is, ", HeightOfTree(root))