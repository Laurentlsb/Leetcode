#Given inorder and postorder traversal of a tree, construct the binary tree. 
#
# Note: 
#You may assume that duplicates do not exist in the tree. 
#
# For example, given 
#
# 
#inorder = [9,3,15,20,7]
#postorder = [9,15,7,20,3] 
#
# Return the following binary tree: 
#
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7
# 
# Related Topics Array Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#12/16/2019
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root_val = postorder[-1]
        index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

"""
原理同105题
只不过后序遍历是最后一个值为根节点
"""
#leetcode submit region end(Prohibit modification and deletion)
