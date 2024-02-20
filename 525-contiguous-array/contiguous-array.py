class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum=0
        prefix_hash={}
        subArr_max=0
        for i in range(len(nums)):
            if nums[i]==0:       #if we encounter 0 we subtract 1 from the sum and we add 1 to the sum if we encounter 1. so if the we find a  subarray whose sum is 0 that means that subarray has equal number of 1's and 0's
                prefix_sum -= 1
            else: 
                prefix_sum +=1
            if prefix_sum==0:
                subArr_max=i+1
            if prefix_sum in prefix_hash:
                ind=prefix_hash.get(prefix_sum)               # if you found the same sum you previously encouterd
                cur_length=i-ind                           # that means the numbers between these sums havenot contributed anything to the 
                subArr_max=max(subArr_max,cur_length)     #sum that you already encounterd so sum of the numbers between these two sums have equal number of 1's and 0's as their sum sum up to 0
            else:
                prefix_hash[prefix_sum]=i
        
        return subArr_max


        