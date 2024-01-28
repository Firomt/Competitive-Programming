class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        zeros=0
        longest_subA=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            
            while zeros > 1:
                if nums[l]==0:
                    zeros-=1
                l+=1
            longest_subA=max(longest_subA, r-l+1-zeros)
        if longest_subA==len(nums):
            return longest_subA-1
        else:
            return longest_subA

    
