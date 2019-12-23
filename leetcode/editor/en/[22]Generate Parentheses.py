#
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
#
# 
#For example, given n = 3, a solution set is:
# 
# 
#[
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
#]
# Related Topics String Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
# 12/22/2019
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, n, '', res)
        return res

    def dfs(self, left, right, path, res):
        if left == right == 0:
            res.append(path)
            return None
        if left > 0:
            self.dfs(left - 1, right, path + '(', res)
        if left < right:
            self.dfs(left, right - 1, path + ')', res)

"""
关键在于想清楚什么情况下是valid combination，在构造解的过程中就已经提前剪枝了
1. 左括号需要先添加，必须始终不小于右括号
2. 只有在右括号少于左括号的时候，才可以添加右括号
只有这样，当left==right==0时，构造出来的，才能确保是有效解
"""
        
#leetcode submit region end(Prohibit modification and deletion)
