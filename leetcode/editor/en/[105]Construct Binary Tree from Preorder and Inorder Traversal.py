#Given preorder and inorder traversal of a tree, construct the binary tree. 
#
# Note: 
#You may assume that duplicates do not exist in the tree. 
#
# For example, given 
#
# 
#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7] 
#
# Return the following binary tree: 
#
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7 
# Related Topics Array Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12/16/2019
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root_val = preorder[0]
        index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
"""
根据前序遍历和中序遍历的性质，重新搭建tree
方法：分治法（递归），不断构造子树
1. 前序遍历的第一个为根节点的值
2. 根据该值在inorder中找根节点的位置，就能分割成左右两个子树
3. 然后递归，找子树的根节点
4. 返回root节点
注意：这里的根节点的索引位置，同样将preorder分割成两个部分，preorder[index+1:]即为右子树的所有节点，前一半的长度等于左子节点加上根节点的个数
""
#leetcode submit region end(Prohibit modification and deletion)
