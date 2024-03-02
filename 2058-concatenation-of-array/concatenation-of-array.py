class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat=nums+[0]*len(nums)
        i=len(nums)
        j=0
        while i in range(len(concat)):
            concat[i]=nums[j]
            i+=1
            j+=1
        return concat

    
        