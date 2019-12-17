#Given a binary tree, flatten it to a linked list in-place. 
#
# For example, given the following tree: 
#
# 
#    1
#   / \
#  2   5
# / \   \
#3   4   6
# 
#
# The flattened tree should look like: 
#
# 
#1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6
# 
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12/16/2019
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if root:
#             node = root
#             while node.left or node.right:
#                 if node.left:
#                     l = node.left
#                     r = node.right
#                     node.right = l
#                     temp = node.right
#                     while temp.right:
#                         temp = temp.right
#                     temp.right = r
#                 node.left = None
#                 node = node.right

# recursively 12/16/2019
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            if root.left:
                l = root.left
                r = root.right
                root.right = l
                temp = root.right
                while temp.right:
                    temp = temp.right
                temp.right = r
            root.left = None
            self.flatten(root.right)
#leetcode submit region end(Prohibit modification and deletion)
