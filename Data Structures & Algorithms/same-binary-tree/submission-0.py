# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer = True
        def inorder(p_root, q_root):
            nonlocal answer
            if not answer: 
                return
            if not p_root and not q_root:
                return
            if not p_root or not q_root:
                answer = False
                return
            inorder(p_root.left, q_root.left)
            inorder(p_root.right, q_root.right)
            if p_root.val != q_root.val:
                answer = False
        inorder(p, q)
        return answer
