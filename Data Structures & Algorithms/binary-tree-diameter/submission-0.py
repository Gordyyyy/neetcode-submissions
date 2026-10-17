# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            result = 0
            leftRemain = self.diameterOfBinaryTree(root.left) 
            rightRemain = self.diameterOfBinaryTree(root.right) 
            leftRemainHeight = self.getMaxHeight(root.left)
            rightRemainHeight = self.getMaxHeight(root.right)
            result = max(
                leftRemain, 
                rightRemain, 
                leftRemainHeight + rightRemainHeight)
            return result


    def getMaxHeight(self,root):
        if root is None:
            return 0
        else:
            height = 0
            leftRemain = self.getMaxHeight(root.left)
            rightRemain = self.getMaxHeight(root.right)
            return 1 + max(leftRemain,rightRemain)