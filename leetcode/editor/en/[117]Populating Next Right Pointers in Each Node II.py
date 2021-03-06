#Given a binary tree 
#
# 
#struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
#}
# 
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. 
#
# Initially, all next pointers are set to NULL. 
#
# 
#
# Follow up: 
#
# 
# You may only use constant extra space. 
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem. 
# 
#
# 
# Example 1: 
#
# 
#
# 
#Input: root = [1,2,3,4,5,null,7]
#Output: [1,#,2,3,#,4,5,7,#]
#Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# 
#
# 
# Constraints: 
#
# 
# The number of nodes in the given tree is less than 6000. 
# -100 <= node.val <= 100 
# 
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 12/17/2019
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        level = [root]
        while level:
            for i in range(len(level)):
                if i+1 == len(level):
                    level[i].next = None
                else:
                    level[i].next = level[i+1]
            pairs = [(node.left, node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
        return root

"""
方法同116题，一模一样
不过不是O(1)的空间复杂度
"""

# reference  O(1)空间复杂度
# def connect(self, node):
#     tail = dummy = TreeLinkNode(0)
#     while node:
#         tail.next = node.left
#         if tail.next:
#             tail = tail.next
#         tail.next = node.right
#         if tail.next:
#             tail = tail.next
#         node = node.next
#         if not node:
#             tail = dummy
#             node = dummy.next
        
#leetcode submit region end(Prohibit modification and deletion)
