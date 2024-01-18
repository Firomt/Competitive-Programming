class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        subArr_max=0
        prefix=0
        prefix_hash={}
        for i in range(len(nums)):
            if nums[i]==0:
                prefix += -1
            else:
                prefix += 1
            if prefix==0:
                subArr_max=i+1
            if prefix in prefix_hash:
                ind=prefix_hash.get(prefix)
                length=i-ind
                subArr_max=max(subArr_max, length)
            else:
                prefix_hash[prefix]=i
        
        return subArr_max


        