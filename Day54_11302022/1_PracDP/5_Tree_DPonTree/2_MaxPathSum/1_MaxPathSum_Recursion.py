#MaxPathSum: any node to any node
import sys
from binarytree import Node
#Function
def MaxPathSum(root):
    global result
    #Base case
    if not root:
        return 0

    #Hypothesis
    left = MaxPathSum(root.left)
    right = MaxPathSum(root.right)

    #Induction
    tempAns = max(root.value + max(left,right),root.value)  #passing on root node; to eliminate the negative node values
    ans = max(tempAns, root.value + left + right) #Include the node
    result = max(result,ans)
    return tempAns 

#Driver code
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

print(root)
result = -1
a= MaxPathSum(root)
print("Max Diameter of tree is,", result)