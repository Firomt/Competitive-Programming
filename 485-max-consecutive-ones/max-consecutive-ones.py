class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i,j=0,0
        max_consec=0
        while j<len(nums):
            if nums[j]>0:
                cur_consec=j-i+1
                max_consec=max(cur_consec,max_consec)
                j+=1
            else:
                i=j+1
                j+=1
        return max_consec
            
        