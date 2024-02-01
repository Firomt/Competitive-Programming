class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        num_set = set(nums)
        
        for j in range(1, len(nums) + 2):
            if j not in num_set:
                return j