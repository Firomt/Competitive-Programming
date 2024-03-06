class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives=[]
        if 0 in nums:
            return 0
        for i in nums:
            if i<0:
                negatives.append(i)
        n=len(negatives)
       
        if n%2==0:
            return 1
        return -1  