# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        if root:
            # in temp_deque, i will store arrays with 2 elements -> first is the node, second is the node's level
            temp_deque = deque()
            temp_deque.append([root, 0])

            while temp_deque:
                curr_node, curr_level = temp_deque.popleft()

                if curr_node.left:
                    temp_deque.append([curr_node.left, curr_level + 1])
                if curr_node.right:
                    temp_deque.append([curr_node.right, curr_level + 1])
                
                if curr_level == len(answer):
                    answer.append(curr_node.val)
                else:
                    answer[curr_level] = curr_node.val
        return answer