class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i < len(nums):
            if nums[i] > n or nums[i] <= 0:
                i+=1
                continue
            elif nums[i]!=i+1:
                correct=nums[i]-1
                if nums[i]!=nums[correct]:
                    nums[i],nums[correct]=nums[correct],nums[i]
                else:
                    i+=1
            else:
                i+=1

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return n+1

        

        
        

