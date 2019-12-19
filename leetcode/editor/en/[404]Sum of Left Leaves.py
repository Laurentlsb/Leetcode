#Find the sum of all left leaves in a given binary tree. 
#
# Example:
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
#There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# 
# Related Topics Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 0)]
        res = 0
        while stack:
            node, flag = stack.pop()
            if not node.left and not node.right and flag == 1:
                res += node.val
            if node.left:
                stack.append((node.left, 1))
            if node.right:
                stack.append((node.right, 0))
        return res

"""
my solution:DFS遍历整个树，并标记每个节点是否是左子节点
"""
        
#leetcode submit region end(Prohibit modification and deletion)
