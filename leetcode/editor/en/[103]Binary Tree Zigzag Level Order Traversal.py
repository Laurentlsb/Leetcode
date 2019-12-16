#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between). 
#
# 
#For example: 
#Given binary tree [3,9,20,null,null,15,7], 
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7
# 
# 
# 
#return its zigzag level order traversal as: 
# 
#[
#  [3],
#  [20,9],
#  [15,7]
#]
# 
# Related Topics Stack Tree Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         parity = 0
#         res = []
#         level = [root]
#         while level:
#             if parity%2 == 0:   # 余数为0，从左向右
#                 res.append([node.val for node in level])
#             else:               # 余数为1，从右向左
#                 res.append([node.val for node in level][::-1])
#             parity += 1
#             pairlist = [(node.left, node.right) for node in level]
#             level = [node for pair in pairlist for node in pair if node]
#         return res

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        level = [root]
        n = 0
        while level:
            if n%2 == 0:
                res.append([node.val for node in level])
            else:
                res.append([node.val for node in level[::-1]])
            n += 1
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
        return res



#leetcode submit region end(Prohibit modification and deletion)
