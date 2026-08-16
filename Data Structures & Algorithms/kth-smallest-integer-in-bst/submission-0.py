# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        curr_val = 0
        answer = 0
        # in order traversal with counter
        def in_order_traversal(root) -> int:
            nonlocal count
            nonlocal curr_val
            nonlocal answer
            if root.left:
                in_order_traversal(root.left)
            curr_val = root.val
            count += 1
            # print(k, count, curr_val)
            if count == k:
                answer = curr_val
                return
            if root.right:
                in_order_traversal(root.right)

        in_order_traversal(root)      
        return answer