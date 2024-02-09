class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        #sort it using cycle sort
        while i < len(nums): 
            correct=nums[i]-1 #for numbers in range[1,n] the correct postion index for the number at nums[i] is i=nums[i]-1
            if nums[i]!= nums[correct]: 
                nums[i],nums[correct]=nums[correct],nums[i]
            elif i!=nums[i]-1 and nums[correct]==nums[i]:#if the element at i hasnt occupied its correct index and if there is another element which is equal to element at i which occupied the correct index then the element at i 
                return nums[i]                           #cant occupyt its correct index as its duplicate has already occupied it so it is the duplicate so return that element
            else:
                i+=1
        return nums[-1] #after putting the numbers at their correct index the last element will be the duplicate as its duplicate has already occupied its index 