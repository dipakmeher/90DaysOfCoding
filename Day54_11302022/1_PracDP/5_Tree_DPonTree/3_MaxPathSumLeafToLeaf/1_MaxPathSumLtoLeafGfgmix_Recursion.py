#MaxPathSum: any leaf to any leaf
import sys
from binarytree import Node
#Function
def MaxPathSum(root):
    global result
    #Base case
    if not root:
        return 0
    
    #Hypothesis
    left = MaxPathSum(root.left) # path sum or height 
    right = MaxPathSum(root.right) # path sum or height 
    print("Root: ", root.value)
    print("left: ",left)
    print("Right: ", right)
    #Induction
    if root.left is not None and root.right is not None: 
        tempAns = max(left,right) + root.value #passing on root node;
        print((not root.left) and (not root.right))
        # if ((not root.left) and (not root.right)):
        #     tempAns = max(tempAns,root.value)# Eliminating the negative node values
        
        print("tempAns: ",tempAns)
        # ans = max(tempAns, root.value + left + right) #Include the node
        # print("ans: ", ans)
        result = max(result,root.value + left + right)
        print("result: ",result)
        print()
        return tempAns # We are returning different value as compare to diameter of tree
    
    if(root.left is None):
        tempAns = right + root.value
        return tempAns
    if root.right is None:
        tempAns = left + root.value
        return tempAns

def MaxPathSumLeafToLeaf(root):
    global result
    a = MaxPathSum(root)
    if root.left and root.right:
        return result
    return max(result, a)


#Driver code
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

result = -1
print(root)
MaxPathSumLeafToLeaf(root)

print("Max Path Sum: Leaf to Leaf is,", result)
