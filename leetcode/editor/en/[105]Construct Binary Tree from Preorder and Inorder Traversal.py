#Given preorder and inorder traversal of a tree, construct the binary tree. 
#
# Note: 
#You may assume that duplicates do not exist in the tree. 
#
# For example, given 
#
# 
#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7] 
#
# Return the following binary tree: 
#
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7 
# Related Topics Array Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root_val = preorder[0]
        index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

#leetcode submit region end(Prohibit modification and deletion)
