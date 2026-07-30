# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else: 
            leftHeight = self.heightOfTree(root.left)
            rightHeight = self.heightOfTree(root.right)
            if abs(leftHeight - rightHeight) > 1:
                self.isEqual = False
            return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            
        self.isEqual = True
        self.heightOfTree(root)
        return self.isEqual
        