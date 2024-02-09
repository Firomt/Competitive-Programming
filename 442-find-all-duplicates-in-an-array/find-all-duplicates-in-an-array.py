class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates=[]
        i=0
        #cycle sort
        while i<len(nums):
            correct=nums[i]-1
            if nums[i] != nums[correct]:
                nums[i], nums[correct]=nums[correct], nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                duplicates.append(nums[i])

        return duplicates 