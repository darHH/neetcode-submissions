# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # thought process 1:
        # root node is always a good node
        # if i am bigger than a good node above me, i will definitely be good too.
        # if i am bigger than a bad node above me, i may or may not be good
        # (have to look upwards until i find anth good node that i am bigger than)
        # thought process 2:
        # dfs and keep track of max seen value
        answer = 0
        def dfs(node, max_seen):
            nonlocal answer
            if node.val >= max_seen:
                answer += 1
                max_seen = node.val
            if node.left:
                dfs(node.left, max_seen)
            if node.right:
                dfs(node.right, max_seen)
        dfs(root, root.val)
        return answer
