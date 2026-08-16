# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first solution timed out:
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         # thought process 1:
#         # from the preorder traversal, we know first element is the root
#         # then from this root node, we can split the inorder traversal to left and right subtree
#         if len(preorder) == 0:
#             return 
#         root_val = preorder[0]
#         if len(preorder) == 1:
#             return TreeNode(root_val)
#         idx = inorder.index(root_val)

#         left_inorder = inorder[:idx]
#         len_left = len(left_inorder)
#         right_inorder = inorder[idx+1:]
#         len_right = len(right_inorder)
#         left_preorder = preorder[1:1+len_left]
#         right_preorder = preorder[1+len_left:]
#         temp_node = TreeNode(root_val)
#         temp_node.left = self.buildTree(left_preorder, left_inorder)
#         temp_node.right = self.buildTree(right_preorder, right_inorder)
#         return temp_node

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_idx = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0
        def helper(left_bound, right_bound):
            nonlocal pre_idx

            if left_bound > right_bound:
                return None
            
            # first element in preorder is the root
            root_val = preorder[pre_idx]
            pre_idx += 1

            if left_bound == right_bound:
                return TreeNode(root_val)

            # root position in inorder list
            root_pos = val_to_idx[root_val]

            temp_node = TreeNode(root_val)
            temp_node.left = helper(left_bound, root_pos - 1)
            temp_node.right = helper(root_pos + 1, right_bound)
            return temp_node

        return helper(0, len(preorder) - 1)