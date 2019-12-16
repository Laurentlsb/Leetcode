# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
#
# Input:     1         1
#          / \       / \
#         2   3     2   3
#
#        [1,2,3],   [1,2,3]
#
# Output: true
#
#
# Example 2:
#
#
# Input:     1         1
#          /           \
#         2             2
#
#        [1,2],     [1,null,2]
#
# Output: false
#
#
# Example 3:
#
#
# Input:     1         1
#          / \       / \
#         2   1     1   2
#
#        [1,2,1],   [1,1,2]
#
# Output: false
#
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

# DFS solution
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p == q == None:
            return True
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            if node_p.val != node_q.val:
                return False

            if node_p.right and node_q.right:
                stack_p.append(node_p.right)
                stack_q.append(node_q.right)
            elif node_p.right == node_q.right == None:
                pass
            else:
                return False

            if node_p.left and node_q.left:
                stack_p.append(node_p.left)
                stack_q.append(node_q.left)
            elif node_p.left == node_q.left == None:
                pass
            else:
                return False
        return True

# # recursion
# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if (not p) and (not q):
#             return True
#         elif (p and not q) or (not p and q):
#             return False
#         elif p and q and p.val!=q.val:
#             return False
#         else:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# leetcode submit region end(Prohibit modification and deletion)

