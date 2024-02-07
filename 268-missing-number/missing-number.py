class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        largest=max(nums)
        for i in range(largest):
            if i not in nums:
                return i
        return largest+1
        