class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #sort it using cycle sort
        #each nums[i] should be at index = nums[i]-1 since it is in the range [1,n]
        i=0
        mismatch=[]
        nums.sort()

        while i < len(nums):
            correct=nums[i]-1
            if nums[i] != nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i] != i+1: #find the number at wrong index(which is the duplicate) 
                mismatch.append(nums[i]) #the duplicate
                mismatch.append(i+1) #the number that is missing 
        return mismatch

        