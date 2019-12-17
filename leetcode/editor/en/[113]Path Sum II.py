#Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum. 
#
# Note: A leaf is a node with no children. 
#
# Example: 
#
# Given the below binary tree and sum = 22, 
#
# 
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \    / \
#7    2  5   1
# 
#
# Return: 
#
# 
#[
#   [5,4,11,2],
#   [5,8,4,5]
#]
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
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            sum_ = 0
            for i in path:
                sum_ += i
            if node.left is None and node.right is None and sum_ == sum:
                res.append(path)
            if node.left:
                stack.append((node.left, path+[node.left.val]))
            if node.right:
                stack.append((node.right, path+[node.right.val]))
        return res
        
#leetcode submit region end(Prohibit modification and deletion)
