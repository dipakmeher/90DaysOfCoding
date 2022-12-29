# Diameter of Tree: Recursion
import sys
from binarytree import Node
#Function
def DiameterOfTree(root):
    global result
    #Base case
    if not root:
        return 0

    #Hypothesis
    left = DiameterOfTree(root.left)
    right = DiameterOfTree(root.right)

    #Induction
    tempAns = 1 + max(left,right) #passing on root node
    ans = max(tempAns,1 + left + right) #Include the node
    result = max(result,ans)
    return tempAns 

#Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = -1
a= DiameterOfTree(root)
print("Max Diameter of tree is,", result)