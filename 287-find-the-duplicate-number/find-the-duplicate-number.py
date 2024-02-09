class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        #sort it using cycle sort
        while i < len(nums): 
            if nums[i] != i+1: #if the current element is not at its correct index
                correct=nums[i]-1 #find the correct index for nums[i]
                if nums[i] != nums[correct]: #if the correct index is not already occupied by its duplicate then swap
                    nums[i], nums[correct]=nums[correct], nums[i]
                else:
                    return nums[i] # correct index is already occupied by its duplicate so return this duplicate
            else:
                i+=1

     
