#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target. 
#
# Each number in candidates may only be used once in the combination. 
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
#Input: candidates = [10,1,2,7,6,1,5], target = 8,
#A solution set is:
#[
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
#]
# 
#
# Example 2: 
#
# 
#Input: candidates = [2,5,2,1,2], target = 5,
#A solution set is:
#[
#  [1,2,2],
#  [5]
#]
# 
# Related Topics Array Backtracking



#leetcode submit region begin(Prohibit modification and deletion)

# 12/20/2019
# recursively
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.helper(candidates, 0, [], target, res)
        return res

    def helper(self, nums, index, path, target, res):
        if target == 0:
            if path not in res:
                res.append(path)
            return None
        elif index >= len(nums) or target < nums[index]:
            return None
        else:
            for i in range(index, len(nums)):
                self.helper(nums, i + 1, path + [nums[i]], target - nums[i], res)

# iteratively

        
#leetcode submit region end(Prohibit modification and deletion)
