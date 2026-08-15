# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, lowest, highest):
            if node is None:
                return True
            if lowest < node.val < highest:
                is_left_valid = True
                is_right_valid = True
                if node.left:
                    is_left_valid = helper(node.left, lowest, node.val)
                if node.right:
                    is_right_valid = helper(node.right, node.val, highest)
                return is_left_valid and is_right_valid
            else:
                return False
        
        return helper(root, float('-inf'), float('inf'))
        