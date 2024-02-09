class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates=[]
        i=0
        #cycle sort
        while i<len(nums):
            if nums[i]!= i+1:
                correct=nums[i]-1
                if nums[i] != nums[correct]:
                    nums[i], nums[correct]=nums[correct], nums[i]
                else:
                    if nums[i] not in duplicates:
                        duplicates.append(nums[i])
                    i+=1
            else:
                i+=1
        return duplicates
        