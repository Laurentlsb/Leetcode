#Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. 
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).” 
#
# Given binary search tree: root = [6,2,8,0,4,7,9,null,null,3,5] 
#
# 
#
# Example 1: 
#
# 
#Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#Output: 6
#Explanation: The LCA of nodes 2 and 8 is 6.
# 
#
# Example 2: 
#
# 
#Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#Output: 2
#Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# 
#
# 
#
# Note: 
#
# 
# All of the nodes' values will be unique. 
# p and q are different and both values will exist in the BST. 
# 
# Related Topics Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12/17/2019
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        node = root
        while node:
            if min(p.val, q.val) <= node.val <= max(p.val, q.val):
                return node
            elif node.val < min(p.val, p.val):
                node = node.right
            elif node.val > max(p.val, q.val):
                 node = node.left

"""
由是BST，所以LCA的值，一定介于p,q之间
这样搜索到的第一个符合条件的node，就一定是LCA
（所以需要分析BST带来的影响，方法比较巧）
"""
#leetcode submit region end(Prohibit modification and deletion)
