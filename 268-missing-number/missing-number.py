class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while i < len(nums):
            if nums[i]==len(nums):
                i+=1
                continue
            correct=nums[i]
            if nums[i] !=  nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
            
    

               
        

  
        