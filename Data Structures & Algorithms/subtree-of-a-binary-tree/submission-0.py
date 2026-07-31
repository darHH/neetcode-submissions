# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(root, subRoot) -> bool:
            if root is None and subRoot is None:
                return True
            elif root is None and subRoot is not None:
                return False
            elif root is not None and subRoot is None:
                return False
            return (root.val == subRoot.val and helper(root.left, subRoot.left) and helper(root.right, subRoot.right))
        

        if root is None or subRoot is None:
            return False
        elif helper(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot))
                
