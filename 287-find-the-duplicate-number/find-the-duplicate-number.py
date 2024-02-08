class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        #sort it using cycle sort
        while i < len(nums): 
            correct=nums[i]-1 #for numbers in range[1,n] the correct postion index for the number at nums[i] is i=nums[i]-1
            if nums[i]!= nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        return nums[-1] #after putting the numbers at their correct index the last element will be the duplicate as its duplicate has already occupied its index 