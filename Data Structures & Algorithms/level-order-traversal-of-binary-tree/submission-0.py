# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        # in temp_array, i will store all the two_val -> so it will be a de queue of arrays with 2 elements
        if root:
            temp_deque = deque()
            temp_deque.append([root, 0])

            while temp_deque:
                # in two_val, i will store the node and its level in a 2 element array
                two_val = []
                curr_node, curr_level = temp_deque.popleft()

                if curr_node.left:
                    temp_deque.append([curr_node.left, curr_level + 1])
                if curr_node.right:
                    temp_deque.append([curr_node.right, curr_level + 1])
                
                if curr_level == len(answer):
                    answer.append([])
                answer[curr_level].append(curr_node.val)

        # print(answer)
        return answer