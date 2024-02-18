class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #solved based on understanding of dutch partioning problem
        i,j=0,0
        k=len(nums)-1
        mid=1
        while j <=k:
            if nums[j] > mid:
                nums[j],nums[k]=nums[k],nums[j]
                k-=1
            elif nums[j] < mid:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            else:
                j+=1

        