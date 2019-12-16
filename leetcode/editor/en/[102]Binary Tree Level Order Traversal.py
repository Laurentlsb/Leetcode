#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level). 
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
#return its level order traversal as: 
# 
#[
#  [3],
#  [9,20],
#  [15,7]
#]
# 
# Related Topics Tree Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        res = []
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
        return res
"""

# class Solution:
#     def levelOrder(self, root):
#         ans, level = [], [root]
#         while root and level:
#             ans.append([node.val for node in level])
#             LRpair = [(node.left, node.right) for node in level] # 以元组的形式，按pair存储
#             level = [leaf for LR in LRpair for leaf in LR if leaf] # 取一个pair，再迭代pair中的非None节点，组成新的一层level
#         return ans


# 12/16/2019
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        level = [root]
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
        return res

#leetcode submit region end(Prohibit modification and deletion)
