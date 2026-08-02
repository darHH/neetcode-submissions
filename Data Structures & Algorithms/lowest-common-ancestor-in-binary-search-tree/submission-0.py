# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # in a bst, values on the left are less than the right.
        # for each node, check if p and q are reachable.
        def isParent(root) -> bool:
            seen_p = False
            seen_q = False
            stack = [root]
            while stack:
                node = stack.pop()
                if node == p:
                    seen_p = True
                if node == q:
                    seen_q = True
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                if seen_p and seen_q:
                    break
            return seen_p and seen_q

        # initial root will always be ancestor
        last_valid = root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if isParent(node):
                last_valid = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return last_valid
    

