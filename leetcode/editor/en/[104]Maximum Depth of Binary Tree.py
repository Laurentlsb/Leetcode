# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
# return its depth = 3.
# Related Topics Tree Depth-first Search
#
#
#
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]
        depth = 0
        while stack:
            current = stack.pop()
            depth = max(depth, current[1])
            if current[0].left is not None:
                pair = (current[0].left, current[1] + 1)
                stack.append(pair)
            if current[0].right is not None:
                pair = (current[0].right, current[1] + 1)
                stack.append(pair)
        return depth

# a basic DFS, use a stack and record the depth, maintain the stack

# leetcode submit region end(Prohibit modification and deletion)
