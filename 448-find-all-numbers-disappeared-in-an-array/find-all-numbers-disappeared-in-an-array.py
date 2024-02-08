class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared=[]
        i=0
        while i < len(nums):
            correct=nums[i]-1
            if nums[i] != nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1

        for i in range(len(nums)):
            if nums[i]!= i+1:
                disappeared.append(i+1)
        return disappeared

        
        