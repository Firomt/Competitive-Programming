class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum=0
        i=0
        while i< len(nums):
            max_sum+=nums[i]
            i+=2
        return max_sum

        