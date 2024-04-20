class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        result = float("inf")
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total >=target:
                result=min(r-l+1, result)
                total-=nums[l]
                l+=1
        if result==float("inf"):
            return 0
        else:
            return result

    
                


            
         
        