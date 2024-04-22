class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        prefix=nums[0]
        for i in range(1,len(nums)):
            prefix+=nums[i]
            nums[i]=prefix
        return nums

        