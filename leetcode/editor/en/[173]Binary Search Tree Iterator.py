#Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST. 
#
# Calling next() will return the next smallest number in the BST. 
#
# 
#
# 
# 
#
# Example: 
#
# 
#
# 
#BSTIterator iterator = new BSTIterator(root);
#iterator.next();    // return 3
#iterator.next();    // return 7
#iterator.hasNext(); // return true
#iterator.next();    // return 9
#iterator.hasNext(); // return true
#iterator.next();    // return 15
#iterator.hasNext(); // return true
#iterator.next();    // return 20
#iterator.hasNext(); // return false
# 
#
# 
#
# Note: 
#
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree. 
# You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called. 
# 
# Related Topics Stack Tree Design



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 12/17/2019
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.array = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            self.array.append(node.val)
            root = node.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.array.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.array else False

"""
由于是BST，所以该题的本质就是按序输出中序遍历的结果
注意stack维护时的操作，易出错
"""

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
#leetcode submit region end(Prohibit modification and deletion)
