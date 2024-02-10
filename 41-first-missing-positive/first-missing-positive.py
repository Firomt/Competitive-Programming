class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #sort it using cycle sort
        i=0
        n=len(nums)
        while i < len(nums):
            if nums[i] > n or nums[i] <= 0:#if nums[i] is greater than length of nums or not positive ignore it
                i+=1
                continue
            elif nums[i]!=i+1: #else according to cycle sort if it isnot at its correct index put it at its correct index
                correct=nums[i]-1
                if nums[i]!=nums[correct]:
                    nums[i],nums[correct]=nums[correct],nums[i]
                else:
                    i+=1
            else:
                i+=1

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1 #after sorting the first index + 1 containing the wrong number is the missing number
        return n+1     #when every number is at its correct index return the next smallest positive which n+1 or max(nums)+1

        
        '''
        more efficient solution
                if not nums:
                    return 1

                num_set = set(nums)
                
                for j in range(1, len(nums) + 2):
                    if j not in num_set:
                        return j

        '''
        
        

