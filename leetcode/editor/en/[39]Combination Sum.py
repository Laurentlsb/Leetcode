#Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target. 
#
# The same repeated number may be chosen from candidates unlimited number of times. 
#
# Note: 
#
# 
# All numbers (including target) will be positive integers. 
# The solution set must not contain duplicate combinations. 
# 
#
# Example 1: 
#
# 
#Input: candidates = [2,3,6,7], target = 7,
#A solution set is:
#[
#  [7],
#  [2,2,3]
#]
# 
#
# Example 2: 
#
# 
#Input: candidates = [2,3,5], target = 8,
#A solution set is:
#[
#  [2,2,2,2],
#  [2,3,3],
#  [3,5]
#]
# 
# Related Topics Array Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
# 12/20/2019
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, temp = [], []
        self.helper(candidates, target, 0, res, temp)
        return res

    def helper(self, candidates, target, index, res, temp):
        if target == 0:
            res.append(temp)
        elif target < candidates[0]:
            pass
        else:
            for i in range(index, len(candidates)):
                # temp.append(candidates[i])  wrong code, just as a reminder
                self.helper(candidates, target - candidates[i], i, res, temp + [candidates[i]])

"""
backtracking
通过回溯candidates，不断用target - num，直到target==0时返回找到的组合
递归的回溯：传参时不能改变原来得temp，否则无法回退到上一个阶段得到的临时组合
"""

# leetcode solution
def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res


def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in xrange(index, len(nums)):
        self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

#leetcode submit region end(Prohibit modification and deletion)
