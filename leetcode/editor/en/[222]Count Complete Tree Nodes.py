#Given a complete binary tree, count the number of nodes. 
#
# Note: 
#
# Definition of a complete binary tree from Wikipedia: 
#In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h. 
#
# Example: 
#
# 
#Input: 
#    1
#   / \
#  2   3
# / \  /
#4  5 6
#
#Output: 6 
# Related Topics Binary Search Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12/17/2019 DFS
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         count = 1
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node.right:
#                 stack.append(node.right)
#                 count += 1
#             if node.left:
#                 stack.append(node.left)
#                 count += 1
#         return count

# reference 方法很巧，因为对于完全二叉树来说，左子树的高度相比右子树，要么相等，要么多一层
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
        
#leetcode submit region end(Prohibit modification and deletion)
