#Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number. 
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123. 
#
# Find the total sum of all root-to-leaf numbers. 
#
# Note: A leaf is a node with no children. 
#
# Example: 
#
# 
#Input: [1,2,3]
#    1
#   / \
#  2   3
#Output: 25
#Explanation:
#The root-to-leaf path 1->2 represents the number 12.
#The root-to-leaf path 1->3 represents the number 13.
#Therefore, sum = 12 + 13 = 25. 
#
# Example 2: 
#
# 
#Input: [4,9,0,5,1]
#    4
#   / \
#  9   0
# / \
#5   1
#Output: 1026
#Explanation:
#The root-to-leaf path 4->9->5 represents the number 495.
#The root-to-leaf path 4->9->1 represents the number 491.
#The root-to-leaf path 4->0 represents the number 40.
#Therefore, sum = 495 + 491 + 40 = 1026. 
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12/17/2019 my solution
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, [root.val])]
        sum_ = 0
        while stack:
            node, path = stack.pop()
            if node.left:
                stack.append((node.left, path + [node.left.val]))
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if not node.left and not node.right:
                sum_ += self.path2num(path)
        return sum_

    def path2num(self, path):
        num = 0
        for i in range(len(path)):
            num += path[i]*10**(len(path)-1-i)
        return num

# # recursively (referrence)
# class Solution:
#     def sumNumbers(self, root):
#         self.res = 0
#         self.dfs(root, 0)
#         return self.res
#
#     def dfs(self, root, value):
#         if root:
#             self.dfs(root.left, value * 10 + root.val)
#             self.dfs(root.right, value * 10 + root.val)
#             if not root.left and not root.right:
#                 self.res += value * 10 + root.val
        
#leetcode submit region end(Prohibit modification and deletion)
