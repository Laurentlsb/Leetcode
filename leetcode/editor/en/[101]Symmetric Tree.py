#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center). 
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric: 
#
# 
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
# 
#
# 
#
# But the following [1,2,2,null,3,null,3] is not: 
#
# 
#    1
#   / \
#  2   2
#   \   \
#   3    3
# 
#
# 
#
# Note: 
#Bonus points if you could solve it both recursively and iteratively. 
# Related Topics Tree Depth-first Search Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# # iteration
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         left_stack = [root]
#         right_stack = [root]
#         while left_stack and right_stack:
#             node_left = left_stack.pop()
#             node_right = right_stack.pop()
#             if (node_left is None and node_right is not None) or (node_left is not None and node_right is None):
#                 return False
#             elif node_left is None and node_right is None:
#                 pass
#
#             if node_left and node_right:
#                 if node_left.val != node_right.val:
#                     return False
#                 else:
#                     left_stack.append(node_left.right)
#                     left_stack.append(node_left.left)
#                     right_stack.append(node_right.left)
#                     right_stack.append(node_right.right)
#         return True

# recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.check(root.left, root.right)

    def check(self, l, r):
        if not l and not r:
            return True
        elif (not l and r) or (l and not r):
            return False
        elif l.val != r.val:
            return False
        else:
            return self.check(l.left, r.right) and self.check(l.right, r.left)
# 递归，比较左右最外侧的边缘节点，再依次向内，对称比较（分析一个最简单的三层结构就好）

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root is None:
#             return True
#
#         if root.left is None and root.right is not None:
#             return False
#         elif root.left is not None and root.right is None:
#             return False
#         elif root.left == root.right is None:
#             return True
#         else:
#             if root.left.val != root.right.val:
#                 return False
#             else:
#                 return self.isSymmetric(root.left) and self.isSymmetric(root.right)
# # wrong idea, since you were checking if the subtree is symmetric



#leetcode submit region end(Prohibit modification and deletion)
